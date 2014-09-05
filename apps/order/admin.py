from django.contrib import admin
from django.http import HttpResponseRedirect, HttpResponse
from apps.order.models import Order, OrderDetail, OrderDelivery, OrderComment
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string
from django.template import Context, RequestContext
from django.conf.urls import patterns, include, url
from django.conf import settings

class OrderDetailInline(admin.StackedInline):
    model = OrderDetail
    extra = 1
    max_num=0

    def get_readonly_fields(self, request, obj):
        if obj:
            return ['product', 'weight', 'surcharge', 'price', 'qty', 'amount']
        else:
            return []
    
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj):
        return False
    
class CommentInline(admin.TabularInline):
    model = OrderComment
    extra = 1

    def get_readonly_fields(self, request, obj):
        if obj:
            return ['user','last_modified']
        else:
            return []
    
class OrderDeliveryInline(admin.StackedInline):
    model = OrderDelivery
    extra = 1

    def get_readonly_fields(self, request, obj):
        if obj:
            return ['country','service','weight','cost']
        else:
            return []

    def has_delete_permission(self, request, obj):
        return False

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_no', 'user', 'amount', 'status', 'status_message', 'order_notes', 'created_on','list_action']
    list_display_links = ['order_no']
    list_filter = ['user', 'status']
    search_fields = ['order_no']
    inlines = [OrderDetailInline, OrderDeliveryInline, CommentInline]

    def list_action(self, obj):
        return '<a href="invoice/'+ str(obj.order_no) +'" target="_blank">Invoice</a>'
    list_action.short_description = "Action"
    list_action.allow_tags = True


    def get_readonly_fields(self, request, obj):
        if obj:
            return self.readonly_fields + ('user', 'order_no', 'amount', 'vat')
        return self.readonly_fields

    def has_add_permission(self, request):
        return False  

    def has_delete_permission(self, request, obj=False):
        return False

    # to auto set user on order comment, when user add comment
    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if isinstance(instance,OrderComment):
                instance.user = request.user
                instance.save()

    # Invoice PDF preview
    def invoice_pdf(self, request, order_no):
        import xhtml2pdf.pisa as pisa
        import cStringIO
        import os
        
        filename = '/pdfs/'+str(order_no)+'.pdf'
        directory = os.path.join(settings.MEDIA_ROOT,'pdfs')
        file_path = settings.MEDIA_ROOT+filename
        if not os.path.exists(directory):
            os.mkdir(directory)

        img = open("static/img/mainlogo.jpg","rb")
        logo = img.read()
        logo_encode = "data:image/jpg;base64,%s" % logo.encode('base64')

        order = Order.objects.select_related('order_delivery').get(order_no=order_no)
        import pdb; pdb.set_trace()
        data = {'order':order, 'logo':logo_encode}
        result = render_to_string('admin/order/invoice.html', data, context_instance=RequestContext(request))
        pdf = pisa.CreatePDF(cStringIO.StringIO(result.encode('UTF-8')), file(file_path, "wb"))

        if not pdf.err:
            pdf.dest.close()
            hasil = {'order':order,'hsl':'OK'}
        else:
            hasil = {'order':order,'hsl':'FAILED'}
        return HttpResponseRedirect('/static/media/'+filename)
        # return render_to_response('admin/order/invoice.html', hasil, context_instance=RequestContext(request))

    def get_urls(self):
        urls = super(OrderAdmin,self).get_urls()
        my_urls = patterns('',(r'^invoice/(\d+)/$',self.invoice_pdf))
        return my_urls + urls

# Register your models here.
admin.site.register(Order, OrderAdmin)
