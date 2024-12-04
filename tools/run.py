from links.models import Link, Tag
from links.utils import gen_short_link
from django.contrib.auth import get_user_model


User = get_user_model()
links = [
    'https://docs.djangoproject.com/en/5.1/',
    'https://hub.docker.com/_/redis',
    'https://yandex.ru/search/?text=django+custom+templatetags+docs',
    'https://www.deepl.com/ru/translator',
    'https://github.com/'
]
tags = {
    'Tag 1': 'tag1',
    'Tag 2': 'tag2',
    'Tag 3': 'tag3',
}


if not User.objects.filter(username='root').exists():
    user = User.objects.create_superuser('root', 'root@example.com', 'root')

for name, slug in tags.items():
    Tag.objects.create(
        name=name,
        slug=slug
    )

for link in links:
    created_link, created = Link.objects.get_or_create(
        source_link=link,
        short_link=gen_short_link(),
        user=user
    )
    created_link.tags.set(Tag.objects.all()[:3])
