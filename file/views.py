from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.encoding import smart_str
from django.utils import timezone
from django.http import HttpResponse
from .models import Files
from django.views.static import serve
import os

# Create your views here.

@login_required()
def file_list(request):
    files = Files.objects.all().order_by('uploaded_datetime')
    return render(request, 'file/file_list.html', {'files':files})

@login_required()
def download_file(request, pk):
    files = Files.objects.all().order_by('uploaded_datetime')
    dl_file = get_object_or_404(Files, pk=pk)
    file_name = dl_file.file_name + '.' + dl_file.extension
    path_to_file = '/var/www/html/' + file_name
    response = HttpResponse(content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
    response['X-Sendfile'] = smart_str(path_to_file)
    return response

