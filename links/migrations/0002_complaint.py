# Generated by Django 5.1.3 on 2024-12-04 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_link', models.CharField(max_length=100, verbose_name='Короткая ссылка')),
                ('description', models.CharField(max_length=1000, verbose_name='Описание жалобы')),
            ],
            options={
                'db_table': 'complaints',
            },
        ),
    ]
