from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from apps.product.models import Part
from datetime import datetime
import string
import random

# Create your models here.

class Order(models.Model):
    STATUS = (('NEW','New Order'),('AWD', 'Awaiting Dispatch'),('CNF','Confirmed'),('SNT','Sent'),('CNL','Cancelled'))

    order_no = models.CharField("Order number",max_length=30, unique=True, null=True)
    user = models.ForeignKey(User,related_name='user_order', null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    vat = models.DecimalField(max_digits=18, decimal_places=2, null=True)    
    status = models.CharField(max_length=10, choices=STATUS, default='NEW')
    status_message = models.TextField("Status message (customer visible)", blank=True, null=True)  
    order_notes = models.TextField(blank=True, null=True)  
    deleted = models.BooleanField(default=False, editable=False)
    created_on = models.DateTimeField("Order date", auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Order"

    def save(self, *args, **kwargs):
        if not self.order_no:
            self.order_no = Order.order_no_generator()
        super(Order, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.order_no

    @classmethod
    def order_no_generator(cls):
        # import pdb; pdb.set_trace()
        latest = cls.objects.all().latest('id')
        size = 8
        chars = string.digits
        random_scring =  ''.join(random.choice(chars) for x in range(size))
        return (str(latest.id+1) + random_scring)[:7]

    def detail_order_data(self):
        order = self.order_detail.all()
        return order

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name="order_detail")
    product = models.ForeignKey(Part, related_name="product")
    weight = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    surcharge = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    price = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    qty = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Order Detail"

    def __unicode__(self):
        return self.product

class OrderDelivery(models.Model):
    order = models.OneToOneField(Order, related_name="order_delivery")
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    business_name = models.CharField(max_length=255, blank=True, null=True)
    address_line1 = models.CharField(max_length=255, null=True)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=10, null=True)
    country = CountryField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=50, null=True)    
    service = models.CharField(max_length=255, null=True)
    weight = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    cost = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Order Delivery"

    def __unicode__(self):
        return self.order

class OrderComment(models.Model):
    order = models.ForeignKey(Order, related_name="order_comment")
    user = models.ForeignKey(User,related_name='user_order_comment',blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Comment"

class Payment(models.Model):
    TYPE = (('WP','Worldpay'),('PP','Paypal'),('SL','Streamline'),('WPVT','WP Virtual Terminal'),('CHQ','Cheque'),('BANK','Bank Transfer'),('CASH','Cash'))

    order = models.ForeignKey(Order, related_name="order_payment")
    payment = models.CharField(max_length=10, choices=TYPE, default='BANK')
    ref = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Payment"

    def __unicode__(self):
        return self.order
