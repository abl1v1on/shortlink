from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Link, Award, LinkAward


@receiver(pre_save, sender=Link)
def track_redirects_count(sender, instance: Link, **kwargs) -> None:
    if instance.pk:
        original_instance: Link = sender.objects.get(pk=instance.pk)
        instance._original_redirects_count = original_instance.redirects_count


@receiver(post_save, sender=Link)
def email_notification(sender, instance: Link, created, **kwargs) -> None:
    """Отслеживаем изменения поля redirects_count"""
    if not created and hasattr(instance, '_original_redirects_count'):
        redirects_count = instance.redirects_count
        if instance._original_redirects_count != redirects_count:
            if redirects_count % 100 == 0:
                try:
                    award = Award.objects.get(redirects_count=redirects_count)
                    LinkAward.objects.create(link=instance, award=award)
                except Award.DoesNotExist:
                    pass
        delattr(instance, '_original_redirects_count')
