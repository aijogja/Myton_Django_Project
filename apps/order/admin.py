from django.contrib import admin
from apps.order.models import Order, OrderDetail, OrderDelivery, OrderComment
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response
from django.template import Context, RequestContext
from django.conf.urls import patterns, include, url

class OrderDetailInline(admin.StackedInline):
    model = OrderDetail
    extra = 1
    max_num=0

    def get_readonly_fields(self, request, obj):
        if obj:
            return ['product','price', 'qty', 'amount']
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
            return ['country','cost']
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
            return self.readonly_fields + ('user','amount','order_no')
        return self.readonly_fields

    def has_add_permission(self, request):
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
        order = Order.objects.get(order_no=order_no)
        data = {'order':order}
        return render_to_response('admin/order/invoice.html', data, context_instance=RequestContext(request))

    def get_urls(self):
        urls = super(OrderAdmin,self).get_urls()
        my_urls = patterns('',(r'^invoice/(\d+)/$',self.invoice_pdf))
        return my_urls + urls

# Register your models here.
admin.site.register(Order, OrderAdmin)
