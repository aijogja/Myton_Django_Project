from django.contrib import admin
from apps.setup.models import PostageCountry, PostageRate, Setting

class PostageCountryAdmin(admin.ModelAdmin):
    list_display = ['country', 'band', 'vat', 'active']
    list_filter = ['band', 'active']

class PostageRateAdmin(admin.ModelAdmin):
    list_display = ['band', 'title', 'postcode', 'weight_start','weight_to','cost','nextday','active']
    list_filter = ['band', 'title', 'active']

class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'value']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj):
        if obj:
            return ['title']
        else:
            return []

# Register your models here.
admin.site.register(PostageCountry, PostageCountryAdmin)
admin.site.register(PostageRate, PostageRateAdmin)
admin.site.register(Setting, SettingAdmin)
