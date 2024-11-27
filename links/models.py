from django.db import models
from django.contrib.auth import get_user_model


class Link(models.Model):
    source_link = models.URLField('Исходная ссылка', max_length=500)
    short_link = models.CharField('Короткая ссылка', max_length=100, unique=True)
    redirects_count = models.PositiveIntegerField('Кол-во переходов', default=0)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='links')

    class Meta:
        db_table = 'links'

    def __str__(self) -> str:
        return self.source_link
