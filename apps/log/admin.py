from django.contrib import admin
from apps.log.models import Search

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

# Register your models here.
admin.site.register(Search,SearchAdmin)
