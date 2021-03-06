from django.contrib import admin
from apps.product.models import Car, Model, Category, DiscountCode, Part, Supplier

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']

class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount']
    ordering = ['code']

class PartAdmin(admin.ModelAdmin):
    actions = None
    list_display = ['part_number', 'name', 'discount_code', 'weight', 'retail_price', 'buy_price', 'surcharge', 'supplier', 'deleted', 'last_modified']
    list_filter = ['discount_code', 'supplier', 'deleted']
    search_fields = ['part_number']

    def has_delete_permission(self, request, obj=False):
        return False

class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact', 'email', 'country', 'active', 'last_modified']

# Register your models here.
admin.site.register(Car)
admin.site.register(Model)
admin.site.register(Category, CategoryAdmin)
admin.site.register(DiscountCode, DiscountCodeAdmin)
admin.site.register(Part, PartAdmin)
admin.site.register(Supplier, SupplierAdmin)