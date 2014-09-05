from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
from django.contrib.sites.models import Site
from datetime import date, datetime, timedelta
from django.db.models import get_model
from apps.product.models import Part
from apps.customer.models import Profile
from Myton_Django.views import calculate_your_price
register = template.Library()

@register.simple_tag
def your_price(request, product_id):
    return calculate_your_price(request,product_id)

@register.simple_tag
def price_inc_tax(price, tax):
    tax_value = float(price)*(float(tax)/100)
    result = float(price)+tax_value
    return '%s' % intcomma(round(result, 2))

@register.simple_tag
def vat_value(price, tax):
    tax_value = float(price)*(float(tax)/100)
    return "%s" % intcomma(round(tax_value, 2))

@register.simple_tag
def vat_value_float(price, tax):
    tax_value = float(price)*(float(tax)/100)
    return "%s" % round(tax_value, 2)

@register.simple_tag
def total_payment(price, tax, delivery_cost):
    tax_value = float(price)*(float(tax)/100)
    result = float(price)+tax_value+float(delivery_cost)    
    return "%s" % intcomma(round(result, 2))

@register.simple_tag
def vat_percent(amount,delivery_cost,vat_value):  
    total = amount - delivery_cost - vat_value
    percent = (vat_value/total)*100
    return '%0.0f' % (percent)

@register.filter(name='currency')
def currency(price):
    cur = '%0.2f' % round(float(price),2)
    return intcomma(cur)

@register.filter(name='subtract')
def subtract(value, arg):
    return value - arg
