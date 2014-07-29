from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import Context, RequestContext
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from forms import MyRegistrationForm
from django.shortcuts import render

#experiment - 03.07.2014 - tomc
from django.http import HttpResponse
from django.template.loader import render_to_string
from trade.models import Part

@login_required
def home(request):
    data = {'breadcrumb':'home'}
    return render_to_response('base.html', data, context_instance=RequestContext(request))

# def login(request):
#     c = {}
#     c.update(csrf(request))
#     return render_to_response('safe_login.html', c)


# def auth_view(request):
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     user = auth.authenticate(username=username, password=password)

#     if user is not None:
#         auth.login(request, user)
#         return HttpResponseRedirect('/accounts/loggedin')
#     else:
#         return HttpResponseRedirect('/accounts/invalid')


# def loggedin(request):
#     return render_to_response('loggedin.html',
#                               {'full_name': request.user.username})


# def invalid_login(request):
    # return render_to_response('invalid_login.html')


# def logout(request):
#     auth.logout(request)
#     return render_to_response('logout.html')

# def register_user(request):
#     if request.method == 'POST':
#         form = MyRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/accounts/register_success')
#     args ={}
#     args.update(csrf(request))

#     args['form'] = MyRegistrationForm()

#     return render_to_response('register.html', args, context_instance=RequestContext(request))

# def register_success(request):
#     return render_to_response('register_success.html')


#some experiments

def ua_display_good1(request):

    var = 001


    return HttpResponse(render_to_string('experiments.html', {'id_number': var}))

#def search(request):
#    if 'q' in request.GET:
#        message = request.GET['q']
#    else:
#        message = 'You submitted an empty form.'
#
#
#    data_received = message
#    return HttpResponse(render_to_string('partsearch.html', {'id_number': data_received}))


def search(request):
    data = {'breadcrumb': 'search'}

    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']

        #perform some operations on the search entered - ie. remove spaces - change all letters to upper case
        q.upper()
        # print q
        q = q.replace(" ", "")
        # print q

        #run a query on the database
        part_object = Part.objects.filter(part_number__icontains=q)
        data['search_query'] = q
        data['part'] = part_object  
    
    return render_to_response('partsearch.html', data, context_instance=RequestContext(request))

