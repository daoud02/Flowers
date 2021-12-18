from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    path('' , views.index , name='index'),
    path('yesterday' , views.yesterday , name='yesterday'),
    path('tomorrow' , views.tomorrow , name='tomorrow'),
]
