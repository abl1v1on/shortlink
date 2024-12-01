import django_filters as filters
from django.forms import Select

from .models import Link


class UserLinkListFilter(filters.FilterSet):
    redirects_ordering = filters.OrderingFilter(
        fields=[
            ('redirects_count', 'redirects_count'),
        ],
        field_labels={
            'redirects_count': 'Количество перенаправлений',
        },
        label='Сортировка по кол-ву перенаправлений',
    )
    date_created_ordering = filters.OrderingFilter(
        fields=[
            ('date_created', 'date_created'),
        ],
        field_labels={
            'date_created': 'Дата создания'
        },
        label='Сортировка по дате создания'
    )

    class Meta:
        model = Link
        fields = {}
