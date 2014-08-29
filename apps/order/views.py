from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, RequestContext
from django.template.loader import render_to_string
from django import forms

from Myton_Django.views import custom_proc
from apps.customer.models import Profile
from apps.customer.forms import DeliveryAddress
from apps.setup.forms import DeliveryServiceForm
from apps.setup.models import PostageRate, PostageCountry, Setting
from apps.order.models import Order, OrderDetail, OrderDelivery
from cart import Cart

# Create your views here.
def get_delivery(request,country):
    if request.is_ajax():
        delivery_form = DeliveryServiceForm()
        tot_weight = request.session['total_weight']
        try:
            check_band = PostageCountry.objects.get(country=country)
            band = check_band.band
            request.session['vat'] = check_band.vat
        except:
            band = ''
        delivery_form.fields['service'] = forms.ModelChoiceField(queryset=PostageRate.objects.all().filter(band=band,active=True,weight_start__lte=tot_weight,weight_to__gte=tot_weight), widget=forms.Select(attrs={'class': 'form-control'}))
        cek = render_to_string('delivery_service_select_form.html', {'delivery_form': delivery_form})

        return HttpResponse(cek)
    else:
        return HttpResponseRedirect('/')

def get_detail_order(request,service):
    # if request.is_ajax():
        profile = Profile.objects.get(user__username=request.user)
        service_rate = PostageRate.objects.get(pk=service)
        cart=Cart(request)

        if request.session['vat'] and not profile.vat_free :
            vat = Setting.objects.get(slug='vat')
            vat = vat.value
        else:
            vat = 0
        data = {'cart':cart, 'service':service_rate, 'vat':vat}
        cek = render_to_string('order/order_detail.html', data, context_instance=RequestContext(request, processors=[custom_proc]))
        return HttpResponse(cek)
    # else:
        # return HttpResponseRedirect('/')

def checkout(request):
    # import pdb; pdb.set_trace()
    cart=Cart(request)
    if cart.count() == 0:
        return HttpResponseRedirect('/my-cart')

    profile = Profile.objects.get(user__username=request.user)
    form = DeliveryAddress(request.POST or None, instance=profile)
    delivery_form = DeliveryServiceForm(request.POST or None)

    if form.is_valid() and delivery_form.is_valid():        
        delivery_cost = delivery_form.cleaned_data['service']
        tot_vat = request.POST.get('tot_vat')
        # import pdb; pdb.set_trace()
        # order data
        order = Order()
        order.user = request.user
        order.amount = float(cart.summary()) + float(delivery_cost.cost) + float(tot_vat)
        order.vat = float(tot_vat)
        order.status = 'NEW'
        order.order_notes = request.POST.get('notes')
        order.save()
        # order detail data
        for ca in cart:
            orderdetail = OrderDetail()
            orderdetail.order = order
            orderdetail.product = ca.product
            orderdetail.weight = ca.product.weight
            orderdetail.surcharge = ca.product.surcharge
            orderdetail.price = ca.unit_price
            orderdetail.qty = ca.quantity
            orderdetail.amount = ca.total_price
            orderdetail.save()
        # order delivery data
        orderdelivery = OrderDelivery ()
        orderdelivery.order = order
        orderdelivery.first_name = form.cleaned_data['first_name']
        orderdelivery.last_name = form.cleaned_data['last_name']
        orderdelivery.business_name = form.cleaned_data['business_name']
        orderdelivery.address_line1 = form.cleaned_data['address_line1']
        orderdelivery.address_line2 = form.cleaned_data['address_line2']
        orderdelivery.city = form.cleaned_data['city']
        orderdelivery.state = form.cleaned_data['state']
        orderdelivery.postcode = form.cleaned_data['postcode']
        orderdelivery.country = form.cleaned_data['country']
        orderdelivery.telephone = form.cleaned_data['telephone']
        orderdelivery.service = delivery_cost.title
        orderdelivery.cost = delivery_cost.cost
        orderdelivery.save()
        cart.clear()
        return HttpResponseRedirect('/')

    try:        
        check_band = PostageCountry.objects.get(country=profile.country)        
        band = check_band.band        
        request.session['vat'] = check_band.vat
    except:
        band = ''    
    tot_weight = request.session['total_weight']    
    delivery_form.fields['service'] = forms.ModelChoiceField(required=True, queryset=PostageRate.objects.all().filter(band=band,active=True,weight_start__lte=tot_weight,weight_to__gte=tot_weight), widget=forms.Select(attrs={'class': 'form-control'}))

    data = {'form':form,'delivery_form':delivery_form}
    return render_to_response('order/checkout.html', data, context_instance=RequestContext(request, processors=[custom_proc]))

def order_complete(request):
    return render_to_response('order_complete.html', data, context_instance=RequestContext(request, processors=[custom_proc]))

def myorder(request):
    myorder = Order.objects.filter(user=request.user)
    data = {'breadcrumb':'myorder', 'order':myorder}
    return render_to_response('order/myorder.html', data, context_instance=RequestContext(request, processors=[custom_proc]))