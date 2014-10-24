from django.shortcuts import render
from django.template import Context, RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from apps.customer.forms import UpdateProfile, MyRegistrationForm
from apps.customer.models import Profile
from Myton_Django.views import custom_proc

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
    return render_to_response('customer/my_detail.html', data, context_instance=RequestContext(request, processors=[custom_proc]))


def register_user(request):
    form = MyRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/accounts/register_success')

    data = {'form': form}
    return render_to_response('customer/register.html', data, context_instance=RequestContext(request, processors=[custom_proc]))


def register_success(request):
    data = {}
    return render_to_response('register_success.html', data, context_instance=RequestContext(request, processors=[custom_proc]))

def change_password(request):
    form = PasswordChangeForm(request.POST)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been updated.")
            return HttpResponseRedirect('/accounts/change_password/')

    data = {'form':form}
    return render_to_response('customer/change_password.html', data, context_instance=RequestContext(request, processors=[custom_proc]))