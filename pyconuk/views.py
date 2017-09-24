import datetime
import os
import posixpath

from django.contrib.staticfiles import finders
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils.six.moves.urllib.parse import unquote
from django.views import static

from .models import Page, Redirection, Sponsor


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
    }

    return render(request, template, context)


def unlinked_pages(request):
    template = 'unlinked_pages.html'

    urls = [
        '/cfp/',
        '/kids/',
        '/pinner-award/',
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
