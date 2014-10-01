from django.contrib import admin
from apps.files.models import Download, ProductList
from Myton_Django.populate import populate_product_by_files
from django_cron import CronJobBase, Schedule


class ProductListAdmin(admin.ModelAdmin):
    list_display = ['title', 'file_upload', 'supplier', 'synced', 'created_on']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('file_upload', 'supplier')
        return self.readonly_fields


class CronProductPrice(CronJobBase):
    #RUN_AT_TIMES = ['1:00']
    RUN_EVERY_MINS = 3

    #schedule = Schedule(run_at_times=RUN_AT_TIMES)
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'files.cron_product_price'

    def do(self):
        try:
            product = ProductList.objects.filter(synced=False).latest('created_on')
            f = open("static/media/" + str(product.file_upload))
            populate_product_by_files(f, product.supplier)
            product.synced = True
            product.save()
        except Exception as e:
            #print '%s (%s)' % (e.message, type(e))
            pass

# Register your models here.
admin.site.register(Download)
admin.site.register(ProductList, ProductListAdmin)
