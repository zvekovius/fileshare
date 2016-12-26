from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    url(r'^$', views.file_list, name='file_list'),
    url(r'^download/(?P<pk>\d+)/$', views.download_file, name='download_file'),
    url(r'^login?(.+)$', auth_view.login),
    url(r'^logout/$', auth_view.logout, {'next_page':'/login'},name='logout'),

]
