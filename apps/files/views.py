from django.shortcuts import render, render_to_response
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required
from apps.files.models import Download

# Create your views here.


@login_required
def list_file_downloads(request):
    file_download = Download.objects.all()
    data = {'breadcrumb': 'downloads', 'data_table': file_download}
    return render_to_response('files/download.html', data, context_instance=RequestContext(request))
