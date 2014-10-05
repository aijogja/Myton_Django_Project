from django.contrib import admin
from apps.files.models import Download, ProductList
from Myton_Django.populate import populate_product_by_files


class ProductListAdmin(admin.ModelAdmin):
    list_display = ['title', 'file_upload', 'supplier', 'synced', 'created_on']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('file_upload', 'supplier')
        return self.readonly_fields

# Register your models here.
admin.site.register(Download)
admin.site.register(ProductList, ProductListAdmin)
