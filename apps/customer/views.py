from django.shortcuts import render
from django.template import Context, RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from apps.customer.forms import UpdateProfile

# Create your views here.


@login_required
def details(request):
	form = UpdateProfile(request.POST or None)
	

	data = {
		'breadcrumb': 'my-details',
		'form': form,
	}
	return render_to_response('customer/my_detail.html', data, context_instance=RequestContext(request))