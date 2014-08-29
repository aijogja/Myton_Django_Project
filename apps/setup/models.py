from django.db import models
from django_countries.fields import CountryField

# Create your models here.

class PostageCountry(models.Model):
    BAND = (('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10'))
    country = CountryField(max_length=100, null=True)
    band = models.CharField(max_length=10, choices=BAND, default='1', null=True)
    vat = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Postage Country"

    def __unicode__(self):
        return '%s' % (self.country)

class PostageRate(models.Model):
    BAND = (('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10'))
    
    band = models.CharField(max_length=10, choices=BAND, default='1', null=True)
    postcode = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    nextday = models.BooleanField(default=False)
    weight_start = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    weight_to = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    cost = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Postage Rate"

    def __unicode__(self):
        return '%s - %s' % (self.title, self.cost)

class Setting(models.Model):    
    title = models.CharField(max_length=225, null=True)    
    slug = models.CharField(max_length=200, null=True, editable=False)
    value = models.CharField(max_length=255, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Setting"

    def __unicode__(self):
        return '%s' % (self.title)
