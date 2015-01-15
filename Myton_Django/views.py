from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import render_to_string
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from forms import MyRegistrationForm
from django.shortcuts import render
from django import forms
# experiment - 03.07.2014 - tomc
from django.http import HttpResponse
# from trade.models import Part
from apps.product.models import Part
from apps.customer.models import Profile
from apps.customer.forms import DeliveryAddress
from apps.setup.forms import DeliveryServiceForm
from apps.setup.models import PostageRate, PostageCountry, Tooltip
from apps.order.models import Order, OrderDetail, OrderDelivery, OrderComment
from apps.log.models import Search
from cart import Cart

def custom_proc(request):
    cart=Cart(request)
    return {
        'user': request.user,
        'cart': cart
    }

@login_required
def home(request):
    return HttpResponseRedirect('/search')    
    # data = {'breadcrumb': 'home'}
    # return render_to_response('base.html', data, context_instance=RequestContext(request, processors=[custom_proc]))

def add_to_cart(request, product_id):
    if request.is_ajax():
        your_price = calculate_your_price(request, product_id)
        part = Part.objects.get(id=product_id)
        # import pdb; pdb.set_trace()
        cart = Cart(request)
        cart.add(part, your_price, part.surcharge, 1)
        return HttpResponse('part added to cart.')
    else:
        return HttpResponseRedirect('/')

@login_required
def mycart(request):
    cart=Cart(request)
    weight = 0
    for ca in cart:
        weight = weight + (float(ca.product.weight) * int(ca.quantity))
    request.session['total_weight'] = weight
    data = {
        'breadcrumb': 'my-cart',
        'cart':cart,
        # 'total_weight' : weight
    }
    return render_to_response('cart.html', data, context_instance=RequestContext(request, processors=[custom_proc]))

@login_required
def clear_cart(request):
    if request.is_ajax():
        cart = Cart(request)
        cart.clear()
        return HttpResponse('cart was destroyed.')
    else:
        return HttpResponseRedirect('/')

@login_required
def update_cart(request, product_id, qty):
    if request.is_ajax():
        your_price = calculate_your_price(request, product_id)
        part = Part.objects.get(id=product_id)
        cart = Cart(request)
        cart.update(part, qty)
        return HttpResponse('part added to cart.')
    else:
        return HttpResponseRedirect('/')

# some experiments

def ua_display_good1(request):

    var = 001

    return HttpResponse(render_to_string('experiments.html', {'id_number': var}))

@login_required
def search(request):
    tooltip = {}
    tooltips = Tooltip.objects.all()
    for ttips in tooltips:
        tooltip[ttips.slug] = ttips.value
    
    data = {'breadcrumb': 'search', 'tooltip': tooltip}

    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']

        # perform some operations on the search entered - ie. remove spaces -
        # change all letters to upper case
        q.upper()
        q = q.replace(" ", "")

        # run a query on the database
        part_object = Part.objects.filter(part_number__icontains=q,deleted=False)
        log_search = Search(user=request.user,keyword=q)
        log_search.save()
        data['search_query'] = q
        data['part'] = part_object

    return render_to_response('product/list_product.html', data, context_instance=RequestContext(request, processors=[custom_proc]))


# Calculating discount band

def calculate_your_price(request, product_id):
    part = Part.objects.get(pk=product_id)
    customer = Profile.objects.get(user=request.user)

    buy_price_1 = part.retail_price / 100
    buy_price_2 = part.discount_code.discount*buy_price_1
    buy_price = part.retail_price - buy_price_2
    split_amount = buy_price_2 / 7
    split_amount_2 = split_amount

    if customer.discount == 'F':
        discount = buy_price + discount_band_F(split_amount, split_amount_2)
    elif customer.discount == 'E':
        discount = buy_price + discount_band_E(split_amount, split_amount_2)
    elif customer.discount == 'D':
        discount = buy_price + discount_band_D(split_amount, split_amount_2)
    elif customer.discount == 'C':
        discount = buy_price + discount_band_C(split_amount, split_amount_2)
    elif customer.discount == 'B':
        discount = buy_price + discount_band_B(split_amount, split_amount_2)
    elif customer.discount == 'A':
        discount = part.retail_price

    return "%.2f" % discount


def discount_band_F(split_amount, split_amount_2):
    split_amount_2 = split_amount_2 + split_amount
    return split_amount_2


def discount_band_E(split_amount, split_amount_2):
    split_amount_2 = discount_band_F (split_amount, split_amount_2)
    split_amount_2 = split_amount_2 + split_amount
    return split_amount_2


def discount_band_D(split_amount, split_amount_2):
    split_amount_2 = discount_band_E (split_amount, split_amount_2)
    split_amount_2 = split_amount_2 + split_amount
    return split_amount_2


def discount_band_C(split_amount, split_amount_2):
    split_amount_2 = discount_band_D (split_amount, split_amount_2)
    split_amount_2 = split_amount_2 + split_amount
    return split_amount_2


def discount_band_B(split_amount, split_amount_2):
    split_amount_2 = discount_band_C (split_amount, split_amount_2)
    split_amount_2 = split_amount_2 + split_amount
    return split_amount_2

def create_pdf(request, order_no):
    from django.conf import settings
    import xhtml2pdf.pisa as pisa
    import cStringIO
    import os
    
    filename = '/pdfs/'+str(order_no)+'.pdf'
    directory = os.path.join(settings.MEDIA_ROOT,'pdfs')
    file_path = settings.MEDIA_ROOT+filename
    if not os.path.exists(directory):
        os.makedirs(directory)

    img = open(os.path.join(settings.BASE_DIR,"static/img/mainlogo.jpg"),"rb")
    logo = img.read()
    logo_encode = "data:image/jpg;base64,%s" % logo.encode('base64')

    order = Order.objects.select_related('order_delivery').get(order_no=order_no)
    total = order.amount - order.order_delivery.cost - order.vat
    vat_percent = '%0.0f' % ((order.vat/total)*100)
    # import pdb; pdb.set_trace()
    data = {'order':order, 'logo':logo_encode, 'vat':vat_percent}
    result = render_to_string('admin/order/invoice.html', data, context_instance=RequestContext(request))
    pdf = pisa.CreatePDF(cStringIO.StringIO(result.encode('UTF-8')), file(file_path, "wb"))
    return filename
