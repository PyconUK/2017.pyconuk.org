from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.page, name='index'),
    url(r'^unlinked-pages/$', views.unlinked_pages, name='unlinked_pages'),
    url(r'^draft-schedule/$', views.schedule_view, name='draft-schedule'),  # TODO rename to schedule
    url(r'^sessions/$', views.sessions_view, name='sessions'),
    url(r'^sessions/(?P<session_type>talk|workshop|keynote|panel)s/(?P<slug>[\w-]+)/$', views.session_view, name='session'),
    url(r'^speakers/$', views.speakers_view, name='speakers'),
    url(r'^speakers/(?P<key>[\w-]+)/$', views.speaker_view, name='speaker'),
    url(r'^sponsors/(?P<key>[\w-]+)/$', views.sponsor_view, name='sponsor'),
    url(r'^(?P<key>.*?)/$', views.page, name='page'),
    url(r'^static/(?P<path>.*)$', views.serve_static),
]
