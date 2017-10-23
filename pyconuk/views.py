import os
import posixpath

from django.contrib.staticfiles import finders
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils.six.moves.urllib.parse import unquote
from django.views import static

from .models import Page, Redirection, Session, Speaker, Sponsor
from .utils import load_schedule_context


def page(request, key='index'):
    try:
        page = Page.objects.get(key=key)
    except Page.DoesNotExist:
        redirection = get_object_or_404(Redirection, key=key)
        template = 'redirection.html'
        context = {'url': redirection.new_url}
        return render(request, template, context)

    assert page.content_format in ['html', 'md'], 'Page content must use HTML or Markdown'

    template = page.template

    context = {
        'content': page.content,
        'content_format': page.content_format,
        'title': page.title,
        'page': page,
        'sponsor_rows': Sponsor.sponsor_rows()
    }

    return render(request, template, context)


def sponsor_view(request, key):
    sponsor = get_object_or_404(Sponsor, key=key)

    template = 'sponsor.html'

    context = {
        'content': sponsor.content,
        'sponsor': sponsor,
        'title': f'Sponsor: {sponsor.name}',
    }

    return render(request, template, context)


def unlinked_pages(request):
    template = 'unlinked_pages.html'

    urls = [
        '/cfp/',
        '/django-girls/',
        '/kids/',
        '/pinner-award/',
        '/sessions/',
        '/session-chairing/',
        '/speakers/',
        '/sponsors/',
        '/tickets/',
        '/transcode/',
        '/board-games/',
    ]

    for redirection in Redirection.objects.order_by('key'):
        urls.append(redirection.original_url)

    context = {
        'urls': urls,
        'title': 'Unlinked pages'
    }

    return render(request, template, context)


def serve_static(request, path, insecure=False, **kwargs):
    """
    This is copied from Django's contrib.staticfiles.views to remove the DEBUG
    check.

    We don't need to check DEBUG since we never actually serve the site with
    Django.

    Serve static files below a given point in the directory structure or
    from locations inferred from the staticfiles finders.
    To use, put a URL pattern such as::
        from django.contrib.staticfiles import views
        url(r'^(?P<path>.*)$', views.serve)
    in your URLconf.
    It uses the django.views.static.serve() view to serve the found files.
    """
    normalized_path = posixpath.normpath(unquote(path)).lstrip('/')
    absolute_path = finders.find(normalized_path)
    if not absolute_path:
        if path.endswith('/') or path == '':
            raise Http404("Directory indexes are not allowed here.")
        raise Http404("'%s' could not be found" % path)
    document_root, path = os.path.split(absolute_path)
    return static.serve(request, path, document_root=document_root, **kwargs)


def schedule_view(request):
    template = 'schedule.html'

    dates = [
        'Thursday 26th',
        'Friday 27th',
        'Saturday 28th',
        'Sunday 29th',
        'Monday 30th'
    ]

    rooms_in_order = {
        'Thursday 26th': [
            'Assembly Room',
            'Room A',
            'Room B',
            'Room C',
            'Ferrier Hall',
        ],
        'Friday 27th': [
            'Assembly Room',
            'Room D',
            'Room C',
            'Room A',
            'Room B',
            'Room I',
            'Room J',
            'Ferrier Hall',
        ],
        'Saturday 28th': [
            'Assembly Room',
            'Ferrier Hall',
            'Room D',
            'Room A',
            'Room I',
            'Room J',
            'Room K',
            'Room L',
            'Room C',
            'Room B',
        ],
        'Sunday 29th': [
            'Assembly Room',
            'Ferrier Hall',
            'Room D',
            'Room C',
            'Room I',
            'Room J',
            'Room K',
            'Room L',
            'Room B',
        ],
        'Monday 30th': [
            'Assembly Room',
            'Ferrier Hall',
            'Room D',
        ],
    }

    schedules = [load_schedule_context(date, rooms_in_order[date]) for date in dates]

    context = {
        'schedules': schedules,
        'title': 'Schedule',
    }

    return render(request, template, context)


def session_view(request, session_type, slug):
    key = '{}/{}'.format(session_type, slug)
    try:
        session = Session.objects.get(key=key)
    except Session.DoesNotExist:
        redirection = get_object_or_404(
            Redirection, key='sessions/{}s/{}'.format(session_type, slug)
        )
        template = 'redirection.html'
        context = {'url': redirection.new_url}
        return render(request, template, context)

    speaker = session.speaker

    assert session.content_format in ['html', 'md'], 'Session content must use HTML or Markdown'

    template = 'session.html'

    context = {
        'content': session.content,
        'content_format': session.content_format,
        'title': session.title,
        'speaker': speaker,
        'track': session.track,
        'day': session.day,
        'time': session.time,
        'room': session.room,
        'video': session.video,
        'slides': session.slides,
    }

    return render(request, template, context)


def sessions_view(request):
    sessions = Session.objects.order_by('title')
    workshops = [s for s in sessions if s.session_type() == 'workshop']
    talks = [s for s in sessions if s.session_type() == 'talk']
    keynotes = [s for s in sessions if s.session_type() == 'keynote']
    others = [s for s in sessions if s.session_type() == 'other']

    template = 'sessions.html'

    context = {
        'workshops': workshops,
        'talks': talks,
        'keynotes': keynotes,
        'otherss': others,
        'title': 'Sessions'
    }

    return render(request, template, context)


def speaker_view(request, key):
    speaker = get_object_or_404(Speaker, key=key)
    sessions = speaker.session_set.all()

    assert speaker.content_format in ['html', 'md'], 'Speaker content must use HTML or Markdown'

    template = 'speaker.html'

    context = {
        'content': speaker.content,
        'content_format': speaker.content_format,
        'name': speaker.name,
        'sessions': sessions,
        'title': speaker.name,
    }

    return render(request, template, context)


def speakers_view(request):
    speakers = Speaker.objects.order_by('name')

    template = 'speakers.html'

    context = {
        'speakers': speakers,
        'title': 'Speakers'
    }

    return render(request, template, context)
