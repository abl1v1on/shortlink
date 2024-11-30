import os
from uuid import uuid4
from typing import Any
from django.views import View
from django.db.models import QuerySet
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.http.request import HttpRequest

from .models import QRCode
from .forms import CreateQRCodeForm
from .tasks import create_qr_task


class UserQRCodesListView(LoginRequiredMixin, ListView):
    template_name = 'qr_codes/qr_codes_list.html'
    context_object_name = 'qr_codes'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мои QR коды'
        return context
    
    def get_queryset(self) -> QuerySet[QRCode]:
        user = self.request.user
        return user.qr_codes.all().prefetch_related('tags')


class CreateQRCodeView(LoginRequiredMixin, CreateView):
    template_name = 'qr_codes/create_qr_code.html'
    form_class = CreateQRCodeForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать QR код'
        return context
    
    def form_valid(self, form: CreateQRCodeForm) -> HttpResponse:
        qr: QRCode = form.save(commit=False)
        user = self.request.user
        unique_id = str(uuid4())

        qr_code_path = f'qr_codes/{unique_id}.jpg'
        qr.user = user
        qr.qr_code_image = qr_code_path
        qr.save()
        form.save_m2m()

        create_qr_task.delay(qr.source_link, unique_id)
        return redirect('qr_codes:user_qr_codes_list')


class DeleteUserQRCodeView(LoginRequiredMixin, View):
    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        qr = get_object_or_404(QRCode, pk=kwargs['qr_id'])

        if qr.user == request.user:
            qr.delete()

        return redirect('qr_codes:user_qr_codes_list')
