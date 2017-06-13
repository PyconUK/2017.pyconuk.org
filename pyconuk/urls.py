from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.page, name='index'),
    url(r'^news/$', views.news_items, name='news_items'),
    url(r'news/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[\w-]+)/$', views.news_item, name='news-item'),
    url(r'^(?P<key>.*?)/$', views.page, name='page'),
    url(r'^static/(?P<path>.*)$', views.serve_static),
]
