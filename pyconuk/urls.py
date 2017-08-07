from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.page, name='index'),
    url(r'^(?P<key>.*?)/$', views.page, name='page'),
    url(r'^static/(?P<path>.*)$', views.serve_static),
]
