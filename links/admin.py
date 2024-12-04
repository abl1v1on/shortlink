from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Link, Tag, Award, Complaint


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
    list_display = ['name', 'show_award']

    @admin.display(description='Иконка')
    def show_award(self, obj: Award):
        return mark_safe(f'<img width="30" src="{obj.icon.url}" alt="{obj.name}" />')


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['short_link', 'description']
