import datetime
import re

from django.db import models
from django_amber.models import ModelWithContent, ModelWithoutContent


class Page(ModelWithContent):
    title = models.CharField(max_length=100)
    template = models.CharField(max_length=20, default='page.html')

    dump_dir_path = 'pages'


class NewsItem(ModelWithContent):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    date = models.DateField()

    dump_dir_path = 'news'

    @classmethod
    def fields_from_key(cls, key):
        pattern = '(?P<year>\d\d\d\d)-(?P<month>\d\d)-(?P<day>\d\d)-(?P<slug>.+)'
        match = re.match(pattern, key)
        groups = match.groupdict()
        date = datetime.datetime(int(groups['year']), int(groups['month']), int(groups['day']))
        return {'date': date, 'slug': groups['slug']}
