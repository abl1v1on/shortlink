from typing import Any
from django.views.generic import ListView, CreateView
from django.db.models import QuerySet

from .models import Link


class UserLinksListView(ListView):
    template_name = 'links/link_list.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мои ссылки'
        return context

    def get_queryset(self) -> QuerySet[Link]:
        user = self.request.user
        return Link.objects.filter(user=user)


class CreateLinkView(CreateView): pass