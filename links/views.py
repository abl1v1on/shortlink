from typing import Any
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from django.http.response import HttpResponse, HttpResponseRedirect
from django.http.request import HttpRequest
from django.db.models import QuerySet
from django.contrib.auth.mixins import LoginRequiredMixin

from . import utils
from .models import Link
from .forms import CreateLinkForm


class UserLinksListView(LoginRequiredMixin, ListView):
    template_name = 'links/link_list.html'
    context_object_name = 'links'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мои ссылки'
        return context

    def get_queryset(self) -> QuerySet[Link]:
        user = self.request.user
        return Link.objects.filter(user=user).prefetch_related('tags')


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
        return redirect('links:user_links_list')


def redirect_to_link(request: HttpRequest, short_link: str) -> HttpResponseRedirect:
    link = get_object_or_404(Link, short_link=short_link)
    link.redirects_count += 1
    link.save()
    return HttpResponseRedirect(link.source_link)
