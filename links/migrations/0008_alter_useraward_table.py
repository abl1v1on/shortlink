# Generated by Django 5.1.3 on 2024-12-01 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0007_alter_useraward_unique_together_useraward_link_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='useraward',
            table='users_awards',
        ),
    ]
