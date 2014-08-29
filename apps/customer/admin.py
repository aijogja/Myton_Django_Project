from django.contrib import admin
from apps.customer.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'business_name', 'first_name', 'last_name','customer_email','telephone','mobile','discount', 'vat_free', 'vat_number']
    list_filter = ['discount']
    search_fields = ['first_name', 'last_name', 'user__email']

    def customer_email(self, obj):
        return obj.user.email
    customer_email.short_description = 'Email'
    customer_email.admin_order_field = 'user__email'

# Register your models here.
admin.site.register(Profile,ProfileAdmin)
