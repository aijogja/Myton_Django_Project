from django.contrib import admin
from apps.setup.models import PostageCountry, PostageRate

class PostageCountryAdmin(admin.ModelAdmin):
    list_display = ['country', 'band', 'vat', 'active']
    list_filter = ['band', 'active']

class PostageRateAdmin(admin.ModelAdmin):
    list_display = ['band', 'title', 'postcode', 'weight_start','weight_to','cost','nextday','active']
    list_filter = ['band', 'title', 'active']

# Register your models here.
admin.site.register(PostageCountry, PostageCountryAdmin)
admin.site.register(PostageRate, PostageRateAdmin)
