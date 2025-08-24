from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.db import models
from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime
from .models import Wallpaper, Tags

class TagsAdmin(admin.ModelAdmin):
    list_display = ('title', 'descr', 'wallpapers_count')
    search_fields = ('title', 'descr')
    
    def wallpapers_count(self, obj):
        return obj.wallpaper_set.count()
    wallpapers_count.short_description = 'Количество обоев'

class WallpaperForm(forms.ModelForm):
    """Form for Wallpaper admin using admin split date/time widget for pub_date."""
    class Meta:
        model = Wallpaper
        fields = '__all__'
        widgets = {
            'pub_date': AdminSplitDateTime(),
        }


    # Ensure the widget brings its admin JS/CSS when the form is used

class WallpaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview', 'pub_date', 'tags_display')
    search_fields = ('title',)
    list_filter = ('tags', 'pub_date')
    filter_horizontal = ('tags',)
    readonly_fields = ('image_preview',)
    fields = ('title', 'image', 'image_preview', 'pub_date', 'tags')
    form = WallpaperForm

    class Media:
        css = {
            'all': ('admin/custom_admin.css',)
        }
        js = (
            'admin/js/core.js',
            'admin/js/calendar.js',
            'admin/js/admin/DateTimeShortcuts.js',
        )

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px; border-radius: 8px;">')
        return 'Нет изображения'
    image_preview.short_description = 'Предпросмотр'

    def tags_display(self, obj):
        tags = obj.tags.all()
        if not tags:
            return '-'
        return format_html(
            '<div class="tags-container">{}</div>',
            mark_safe(' '.join([
                f'<span class="chip">{tag.title}</span>'
                for tag in tags
            ]))
        )
    tags_display.short_description = 'Теги'

admin.site.register(Wallpaper, WallpaperAdmin)
admin.site.register(Tags, TagsAdmin)