from django.contrib import admin
from apps.files.models import Download, ProductList
from Myton_Django.populate import populate_product_by_files

class ProductListAdmin(admin.ModelAdmin):
    list_display = ['title' ,'file_upload','created_on']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('file_upload',)
        return self.readonly_fields

    def save_model(self, request, obj,form, change):  
        obj.save()  	
        url = obj.file_upload.url[1:]
        f = open(url)
        # Call script to populate data into db
        populate_product_by_files(f)

# Register your models here.
admin.site.register(Download)
admin.site.register(ProductList, ProductListAdmin)
