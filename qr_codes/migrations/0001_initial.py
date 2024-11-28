# Generated by Django 5.1.3 on 2024-11-28 02:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('links', '0004_alter_link_tags'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QRCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_link', models.URLField(max_length=500, verbose_name='Исходная ссылка')),
                ('redirects_count', models.PositiveIntegerField(default=0, verbose_name='Кол-во переходов')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('qr_code_image', models.ImageField(upload_to='qr_codes/', verbose_name='QR')),
                ('tags', models.ManyToManyField(blank=True, related_name='qr_codes', to='links.tag', verbose_name='Теги')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qr_codes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'qr_codes',
            },
        ),
    ]
