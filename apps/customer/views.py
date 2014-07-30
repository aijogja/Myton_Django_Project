from django.shortcuts import render
from django.template import Context, RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.customer.forms import UpdateProfile, MyRegistrationForm
from apps.customer.models import Profile

# Create your views here.


@login_required
def details(request):
    profile = Profile.objects.get(user__username=request.user)
    form = UpdateProfile(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        messages.success(request, "Your profile has been updated.")

    data = {
        'breadcrumb': 'my-details',
        'form': form,
    }
    return render_to_response('customer/my_detail.html', data, context_instance=RequestContext(request))


def register_user(request):
    form = MyRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/accounts/register_success')

    data = {'form': form}
    return render_to_response('customer/register.html', data, context_instance=RequestContext(request))


def register_success(request):
    data = {}
    return render_to_response('register_success.html', data, context_instance=RequestContext(request))
