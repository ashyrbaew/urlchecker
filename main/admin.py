from django.contrib import admin

from main.models import Urls


@admin.register(Urls)
class UrlsAdmin(admin.ModelAdmin):
    readonly_fields = ['created_on', 'updated_on']
    list_display = ['title', 'url', 'is_active', 'update_interval',
                    'status_code', 'user'] + readonly_fields
    fields = ('title', 'url', 'is_active', 'update_interval', 'status_code',
              'user')
