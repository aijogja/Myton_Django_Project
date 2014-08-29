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
    return result

@register.simple_tag
def vat_value(price, tax):
    tax_value = float(price)*(float(tax)/100)
    return tax_value

@register.simple_tag
def total_payment(price, tax, delivery_cost):
    tax_value = float(price)*(float(tax)/100)
    result = float(price)+tax_value+float(delivery_cost)
    return result
