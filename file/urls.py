from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.file_list, name='file_list'),
    url(r'^download/(?P<pk>\d+)/$', views.download_file, name='download_file'),
]
