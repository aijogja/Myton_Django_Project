from django.db import models
from smart_selects.db_fields import ChainedForeignKey, GroupedForeignKey

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
        verbose_name_plural = "DiscountCode"

    def __unicode__(self):
        return self.code

class Part(models.Model):
    part_number = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=255, null=True)
    supersessions = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='part', null=True)
    car = models.ForeignKey(Car,related_name='car_part', null=True)
    # model = models.ForeignKey(Model,related_name='model', null=True)
    model = ChainedForeignKey(Model, chained_field="car", chained_model_field="car", null=True)
    category = models.ForeignKey(Category,related_name='category', null=True)
    chassis_range = models.CharField(max_length=50, blank=True, null=True)
    derivitive = models.CharField(max_length=50, blank=True, null=True)
    year = models.CharField(max_length=50, blank=True, null=True)
    weight = models.FloatField(blank=True,null=True)
    discount_code = models.ForeignKey(DiscountCode,related_name='discount_code', null=True)
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


