from django.contrib import admin
from apps.order.models import Order, OrderDetail, OrderDelivery, OrderComment

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
    list_display = ['order_no', 'user', 'amount', 'status', 'status_message', 'order_notes', 'created_on']
    list_display_links = ['order_no']
    list_filter = ['user', 'status']
    search_fields = ['order_no']
    inlines = [OrderDetailInline, OrderDeliveryInline, CommentInline]

    def get_readonly_fields(self, request, obj):
        if obj:
            return self.readonly_fields + ('user','amount','order_no')
        return self.readonly_fields

    def has_add_permission(self, request):
        return False  

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if isinstance(instance,OrderComment):
                instance.user = request.user
                instance.save()

# Register your models here.
admin.site.register(Order, OrderAdmin)
