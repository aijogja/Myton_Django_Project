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

