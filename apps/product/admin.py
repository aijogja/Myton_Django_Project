from django.contrib import admin
from apps.product.models import Car, Model, Category, DiscountCode, Part
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']

class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount']
    ordering = ['code']

class PartAdmin(admin.ModelAdmin):
    list_display = ['part_number', 'name', 'discount_code', 'retail_price', 'buy_price']

admin.site.register(Car)
admin.site.register(Model)
admin.site.register(Category, CategoryAdmin)
admin.site.register(DiscountCode, DiscountCodeAdmin)
admin.site.register(Part, PartAdmin)