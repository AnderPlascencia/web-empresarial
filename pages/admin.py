from django.contrib import admin
from .models import Page
from django.template.defaultfilters import truncatechars

# Register your models here.

        
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'short_description', 'order')

    def short_description(self, obj):
        return truncatechars(obj.content, 200)
    short_description.short_description = "descripción"

admin.site.register(Page, PageAdmin)