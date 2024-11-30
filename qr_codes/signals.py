import os
from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import QRCode


@receiver(post_delete, sender=QRCode)
def delete_qr_code_image(sender, instance: QRCode, **kwargs) -> None:
    if instance.qr_code_image and os.path.exists(instance.qr_code_image.path):
        instance.qr_code_image.delete(save=False)
