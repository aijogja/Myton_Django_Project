from django.contrib import admin
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string
from django.template import Context, RequestContext
from django.conf.urls import patterns, include, url
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.contrib import messages
from Myton_Django.views import custom_proc, create_pdf
from apps.order.models import Order, OrderDetail, OrderDelivery, OrderComment
from apps.order.forms import Send_email

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
        return '<a href="invoice/'+ str(obj.order_no) +'" target="_blank">Invoice</a> | '+'<a href="send_email/'+ str(obj.order_no) +'">Send Email</a>'
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
        filename = create_pdf(request, order_no)
        return HttpResponseRedirect('/static/media/'+filename)

    def send_email(self, request, order_no):
        order = Order.objects.get(order_no=order_no)
        form = Send_email(request.POST or None, initial={'email':order.user.email})
        if form.is_valid():
            to = form.cleaned_data['email']
            subject = '[Myton Automotive] '+form.cleaned_data['subject']
            body = form.cleaned_data['body']
            # import pdb; pdb.set_trace()
            email = EmailMessage(subject, body, 'aijogjadab@gmail.com', [to])
            email.content_subtype = "html"  # Main content is now text/html
            email.send(fail_silently=False)
            messages.success(request, "The email to \""+to+"\" for order \""+order_no+"\" was sent successfully.")
            return HttpResponseRedirect('/admin/order/order/')
        
        data = {
            'form':form,
            'title':'Send email',
        }
        return render_to_response('admin/order/send_mail.html', data, context_instance=RequestContext(request))

    def get_urls(self):
        urls = super(OrderAdmin,self).get_urls()
        my_urls = patterns('',
            (r'^invoice/(\d+)/$',self.invoice_pdf),
            (r'^send_email/(\d+)/$',self.send_email)
            )
        return my_urls + urls

# Register your models here.
admin.site.register(Order, OrderAdmin)
