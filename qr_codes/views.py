from uuid import uuid4
from typing import Any
from datetime import datetime
from django.db.models import QuerySet
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse

from .models import QRCode
from .forms import CreateQRCodeForm
from .utils import create_qr


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
        qr_code_path = create_qr(qr.source_link, str(uuid4()))
        qr.user = user
        qr.qr_code_image = qr_code_path
        qr.save()
        return redirect('qr_codes:user_qr_codes_list')
