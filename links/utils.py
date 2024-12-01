from uuid import uuid4
from django.db.models import QuerySet
from django.contrib.auth.models import User

from .models import Link


def gen_short_link() -> str:
    return str(uuid4()).split('-')[0]


def get_user_links(user: User) -> QuerySet[Link]:
    return user.links.all().prefetch_related('tags', 'awards')
