from django.contrib import admin
from datetime import timedelta
from apps.log.models import Search, Session

class SearchAdmin(admin.ModelAdmin):
    actions = None
    list_display = ['keyword', 'user', 'created_on']
    list_filter = ['user']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('user', 'keyword')
        return self.readonly_fields

class SessionAdmin(admin.ModelAdmin):
    actions = None
    list_display = ['session_key', 'user', 'ipaddress', 'convert_time_on_site', 'created_on']

    def convert_time_on_site(self, obj):
        if obj.time_on_site is not None:
            return timedelta(seconds=obj.time_on_site)
    convert_time_on_site.short_description = 'Time Online'
    convert_time_on_site.admin_order_field = 'time_on_site'

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('session_key', 'user', 'ipaddress')
        return self.readonly_fields

# Register your models here.
admin.site.register(Search,SearchAdmin)
admin.site.register(Session,SessionAdmin)
