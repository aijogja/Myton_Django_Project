from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import render_to_string
from django import forms

from Myton_Django.views import custom_proc
from apps.customer.models import Profile
from apps.customer.forms import DeliveryAddress
from apps.setup.forms import DeliveryServiceForm
from apps.setup.models import PostageRate, PostageCountry
from cart import Cart

# Create your views here.

def checkout(request):
    profile = Profile.objects.get(user__username=request.user)
    form = DeliveryAddress(request.POST or None, instance=profile)
    delivery_form = DeliveryServiceForm(request.POST or None)

    if form.is_valid() and delivery_form.is_valid():
        import pdb; pdb.set_trace()
        
        pass        

    try:        
        check_band = PostageCountry.objects.get(country=profile.country)
        band = check_band.band
    except:
        band = '1'
    delivery_form.fields['service'] = forms.ModelChoiceField(required=True, queryset=PostageRate.objects.all().filter(band=band), widget=forms.Select(attrs={'class': 'form-control'}))

    data = {'form':form,'delivery_form':delivery_form}
    return render_to_response('checkout.html', data, context_instance=RequestContext(request, processors=[custom_proc]))
