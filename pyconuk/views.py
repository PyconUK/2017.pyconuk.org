import datetime
import os
import posixpath

from django.contrib.staticfiles import finders
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils.six.moves.urllib.parse import unquote
from django.views import static

from .models import NewsItem, Page


def page(request, key='index'):
    page = get_object_or_404(Page, key=key)
    assert page.content_format in ['html', 'md'], 'Page content must use HTML or Markdown'

    template = page.template

    context = {
        'content': page.content,
        'content_format': page.content_format,
        'title': page.title,
    }

    return render(request, template, context)


def news_items(request):
    news_items = NewsItem.objects.order_by('-date')

    template = 'news_items.html'

    context = {
        'news_items': news_items,
        'title': 'News',
    }

    return render(request, template, context)


def news_item(request, year, month, day, slug):
    date = datetime.date(int(year), int(month), int(day))
    news_item = get_object_or_404(NewsItem, slug=slug, date=date)

    assert news_item.content_format in ['html', 'md'], 'NewsItem content must use HTML or Markdown'

    template = 'news_item.html'

    context = {
        'content': news_item.content,
        'content_format': news_item.content_format,
        'title': news_item.title,
        'date': news_item.date,
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
