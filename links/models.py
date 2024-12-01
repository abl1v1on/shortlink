from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Link(models.Model):
    source_link = models.URLField('Исходная ссылка', max_length=500)
    short_link = models.CharField('Короткая ссылка', max_length=100, unique=True)
    redirects_count = models.PositiveIntegerField('Кол-во переходов', default=0)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='links')
    date_created = models.DateField(auto_now_add=True, editable=False)
    tags = models.ManyToManyField(
        'Tag', 
        related_name='links', 
        verbose_name='Теги', 
        blank=True, 
    )

    class Meta:
        db_table = 'links'
        ordering = ['-redirects_count']

    def get_absolute_url(self):
        return reverse('links:redirect_to_link', kwargs={'short_link': self.short_link})

    def __str__(self) -> str:
        return self.source_link


class Tag(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)
    slug = models.SlugField('URL', max_length=50, db_index=True, unique=True)

    class Meta:
        db_table = 'tags'
    
    def __str__(self) -> str:
        return self.name


class Award(models.Model):    
    name = models.CharField('Название', max_length=70, unique=True)
    icon = models.ImageField('Иконка', upload_to='awards')
    redirects_count = models.PositiveIntegerField('Кол-во переходов для награды')
    link = models.ManyToManyField(Link, through='LinkAward', related_name='awards')

    class Meta:
        db_table = 'awards'

    def __str__(self) -> str:
        return self.name


class LinkAward(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    date_of_assignment = models.DateField('Дата присвоения', auto_now_add=True)

    class Meta:
        db_table = 'links_awards'
        unique_together = ('award', 'link')

    def __str__(self) -> str:
        return self.award.name
