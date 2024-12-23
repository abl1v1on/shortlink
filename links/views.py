from typing import Any
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView
from django.http.response import HttpResponse, HttpResponseRedirect
from django.http.request import HttpRequest
from django.db.models import QuerySet
from django.contrib.auth.mixins import LoginRequiredMixin

from . import utils
from .models import Link, Complaint
from .forms import CreateLinkForm, CreateComplaintForm
from .filters import UserLinkListFilter


class UserLinksListView(LoginRequiredMixin, ListView):
    template_name = 'links/link_list.html'
    context_object_name = 'links'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мои ссылки'
        context['filter_form'] = self.get_filter().form
        return context

    def get_queryset(self) -> QuerySet[Link]:
        return self.get_filter().qs

    def get_filter(self) -> UserLinkListFilter:
        user = self.request.user
        return UserLinkListFilter(self.request.GET, utils.get_user_links(user))


class CreateLinkView(LoginRequiredMixin, CreateView):
    template_name = 'links/create-link.html'
    form_class = CreateLinkForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать ссылку'
        return context
    
    def form_valid(self, form: CreateLinkForm) -> HttpResponse:
        link: Link = form.save(commit=False)
        link.short_link = utils.gen_short_link()
        link.user = self.request.user
        link.save()
        form.save_m2m()
        return redirect('links:user_links_list')


class DeleteUserLinkView(LoginRequiredMixin, View):
    """
    Юзаем View а не DeleteView так как нам не нужна
    страница подтверждения удаления
    """
    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        link = get_object_or_404(Link, pk=kwargs['link_id'])

        if link.user == request.user:
            link.delete()

        return redirect('links:user_links_list')


class TopUserLinksView(LoginRequiredMixin, ListView):
    template_name = 'links/top_links.html'
    context_object_name = 'links'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)    
        context['title'] = 'Топ 10 ссылок'
        return context

    def get_queryset(self) -> QuerySet[Link]:
        return Link.objects.order_by('-redirects_count') \
            .select_related('user') \
            .prefetch_related('tags')[:10]


class CreateComplaintView(CreateView):
    model = Complaint
    template_name = 'links/create_complaint.html'
    form_class = CreateComplaintForm
    success_url = reverse_lazy('links:user_links_list')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Оставить жалобу'
        return context


def redirect_to_link(request: HttpRequest, short_link: str) -> HttpResponseRedirect:
    link = get_object_or_404(Link, short_link=short_link)
    link.redirects_count += 1
    link.save()
    return HttpResponseRedirect(link.source_link)
