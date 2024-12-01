# Generated by Django 5.1.3 on 2024-12-01 00:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0006_award_redirects_count_alter_award_icon'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='useraward',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='useraward',
            name='link',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='links.link'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='useraward',
            unique_together={('user', 'award', 'link')},
        ),
    ]