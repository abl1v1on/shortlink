# Generated by Django 5.1.3 on 2024-11-28 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_codes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='qr_code_image',
            field=models.ImageField(max_length=300, upload_to='qr_codes/', verbose_name='QR'),
        ),
    ]
