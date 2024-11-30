from django.contrib import admin

from .models import Link, Tag, Award


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['source_link', 'short_link', 'redirects_count', 'date_created']
    readonly_fields = list_display
    list_display_links = ['source_link']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ['name']
