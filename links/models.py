from django.db import models
from django.contrib.auth import get_user_model


class Link(models.Model):
    source_link = models.URLField('Исходная ссылка', max_length=500)
    short_link = models.CharField('Короткая ссылка', max_length=100, unique=True)
    redirects_count = models.PositiveIntegerField('Кол-во переходов', default=0)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='links')
    date_created = models.DateField(auto_now_add=True, editable=False)
    tags = models.ManyToManyField('Tag', related_name='links', verbose_name='Теги')

    class Meta:
        db_table = 'links'

    def __str__(self) -> str:
        return self.source_link


class Tag(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)
    slug = models.SlugField('URL', max_length=50, db_index=True, unique=True)

    class Meta:
        db_table = 'tags'
    
    def __str__(self) -> str:
        return self.name
