from django.db import models
from django.contrib.auth import get_user_model

from links.models import Tag


class QRCode(models.Model):
    source_link = models.URLField('Исходная ссылка', max_length=500)
    redirects_count = models.PositiveIntegerField('Кол-во переходов', default=0)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='qr_codes')
    date_created = models.DateField(auto_now_add=True, editable=False)
    tags = models.ManyToManyField(
        Tag, 
        related_name='qr_codes', 
        verbose_name='Теги', 
        blank=True, 
    )
    qr_code_image = models.ImageField('QR', upload_to='qr_codes/')

    class Meta:
        db_table = 'qr_codes'
