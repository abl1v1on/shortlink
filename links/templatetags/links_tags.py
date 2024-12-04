from django import template
from django.db.models import QuerySet

from links.models import Link


register = template.Library()


@register.inclusion_tag('links/base_link_list.html')
def show_link_list(links: QuerySet[Link], is_user_links: bool):
    return {'links': links, 'is_user_links': is_user_links}
