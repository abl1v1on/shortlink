from django.apps import AppConfig


class QrCodesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'qr_codes'

    def ready(self):
        import qr_codes.signals
