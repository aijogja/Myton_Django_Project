from django.db import models
from smart_selects.db_fields import ChainedForeignKey, GroupedForeignKey
from django_countries.fields import CountryField

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Car"

    def __unicode__(self):
        return self.name

class Model(models.Model):
    car = models.ForeignKey(Car, related_name="car")
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Model"

    def __unicode__(self):
        return self.name

class Category(models.Model):
    parent = models.ForeignKey("self",related_name='parent_category',blank=True, null=True)
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Category"

    def __unicode__(self):
        return self.name

class DiscountCode(models.Model):
    code = models.CharField(max_length=5, null=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Discount Code"

    def __unicode__(self):
        return self.code


class Supplier(models.Model):
    name = models.CharField(max_length=255, null=True)
    contact = models.CharField(max_length=255, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=255, null=True)
    address = models.TextField(blank=True, null=True) 
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=10, blank=True, null=True)
    country = CountryField(max_length=100, blank=True, null=True)  
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Supplier"

    def __unicode__(self):
        return self.name

class Part(models.Model):
    QUALITY_CHOICE = (('GEN','Genuine'),('OEM', 'OEM'),('AFM','Aftermarket'),('RCD','Reconditioned'),('USE','Used'))

    part_number = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=255, null=True)
    supersessions = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='part',blank=True, null=True)
    car = models.ForeignKey(Car,related_name='car_part',blank=True, null=True)
    model = ChainedForeignKey(Model, chained_field="car", chained_model_field="car",blank=True, null=True)
    category = models.ForeignKey(Category,related_name='category',blank=True, null=True)
    chassis_range = models.CharField(max_length=50, blank=True, null=True)
    derivitive = models.CharField(max_length=50, blank=True, null=True)
    year = models.CharField(max_length=50, blank=True, null=True)    
    discount_code = models.ForeignKey(DiscountCode,related_name='discount_code', null=True)
    supplier = models.ForeignKey(Supplier, related_name='part_supplier', blank=True, null=True)
    quality = models.CharField(max_length=10, choices=QUALITY_CHOICE, default='GEN', blank=True, null=True)
    weight = models.DecimalField(max_digits=18, decimal_places=2, default=1, null=True)
    height = models.DecimalField(max_digits=18, decimal_places=2, default=1, null=True)
    width = models.DecimalField(max_digits=18, decimal_places=2, default=1, null=True)
    length = models.DecimalField(max_digits=18, decimal_places=2, default=1, null=True)
    retail_price = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    buy_price = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    surcharge = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    deleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Part"

    def __unicode__(self):
        return self.part_number



