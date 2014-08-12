from django.db import models
from django.contrib.auth.models import User
from apps.product.models import Part

# Create your models here.

class Order(models.Model):
	AWD = 'Awaiting Dispatch'
	STATUS = ((AWD, 'Awaiting Dispatch'))

	order_no = models.DecimalField(max_length=30, null=True)
    user = models.ForeignKey(User,related_name='user_order', null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    status = models.CharField(max_length=10, choices=STATUS, default=NEW)
    status_message = models.TextField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Order"

    def __unicode__(self):
        return self.order_no

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name="order")
    product = models.ForeignKey(Part, related_name="product")
    price = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    qty = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=18, decimal_places=2, null=True)
