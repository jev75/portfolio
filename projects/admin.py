from django.contrib import admin
from django.utils.html import format_html, strip_tags
from django.utils.safestring import mark_safe
import html
from .models import Project, Category, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_display')
    ordering = ('title',)

    def image_display(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="auto" />', obj.image.url)
        return ''
    image_display.short_description = 'Nuotrauka'

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'clean_summary', 'image_display')
    list_filter = ('category',)
    search_fields = ('title', 'description')
    ordering = ('title',)

    def summary(self, obj):
        return obj.description[:100] if obj.description else ''
    summary.short_description = 'Santrauka'

    def clean_summary(self, obj):
        return mark_safe(html.unescape(strip_tags(self.summary(obj))))
    clean_summary.short_description = 'Santrauka'

    def image_display(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="auto" />', obj.image.url)
        return ''
    image_display.short_description = 'Nuotrauka'

admin.site.register(Review)