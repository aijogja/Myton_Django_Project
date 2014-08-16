from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from apps.product.models import Part
import string
import random

# Create your models here.

class Order(models.Model):
    STATUS = (('NEW','New Order'),('AWD', 'Awaiting Dispatch'),('CNL','Cancelled'),('CNF','Confirmed'))

    order_no = models.CharField(max_length=30, null=True)
    user = models.ForeignKey(User,related_name='user_order', null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    status = models.CharField(max_length=10, choices=STATUS, default='NEW')
    status_message = models.TextField(blank=True, null=True)  
    order_notes = models.TextField(blank=True, null=True)  
    deleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Order"

    def save(self, *args, **kwargs):
        random_string = ''.join(random.choice(string.digits) for i in range(5))
        self.order_no = random_string
        super(Order, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.order_no

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name="order")
    product = models.ForeignKey(Part, related_name="product")
    price = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    qty = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

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
    cost = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
