from django.shortcuts import render, get_object_or_404
from django.utils.encoding import smart_str
from django.utils import timezone
from django.http import HttpResponse
from .models import Files

# Create your views here.

def file_list(request):
    files = Files.objects.all().order_by('uploaded_datetime')
    return render(request, 'file/file_list.html', {'files':files})

def download_file(request, pk):
    files = Files.objects.all().order_by('uploaded_datetime')
    dl_file = get_object_or_404(Files, pk=pk)
    file_name = dl_file.file_name
    path_to_file = '/home/zvekovius/test/' + file_name
    response = HttpResponse(content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
    response['X-Sendfile'] = smart_str(path_to_file)
    return response

    #return render(request, 'file/download_file.html', {'file':dl_file})
