from django.contrib import admin

from .models import QRCode


@admin.register(QRCode)
class QRCodeAdmin(admin.ModelAdmin):
    list_display = ['source_link', 'redirects_count', 'date_created']
    list_display_links = ['source_link']
