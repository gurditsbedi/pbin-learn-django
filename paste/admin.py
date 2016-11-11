from django.contrib import admin

from .models import pasteModel

class pasteAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'text', 'timestamp']

admin.site.register(pasteModel, pasteAdmin)