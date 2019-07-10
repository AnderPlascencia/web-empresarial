from django.contrib import admin
from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')
    list_per_page = 10 

admin.site.register(Service, ServiceAdmin)