import datetime
import re

from django.db import models
from django_amber.models import ModelWithContent, ModelWithoutContent


class Page(ModelWithContent):
    title = models.CharField(max_length=100)
    template = models.CharField(max_length=20, default='page.html')
    show_sponsors = models.BooleanField(default=True)

    dump_dir_path = 'pages'


class Redirection(ModelWithoutContent):
    new_url = models.CharField(max_length=255)

    dump_dir_path = 'redirections'

    def original_url(self):
        return '/{}/'.format(self.key)


class Sponsor(ModelWithContent):
    TIERS = (
        ('gold', 'gold'),
        ('silver', 'silver'),
        ('bronze', 'bronze'),
        ('partner', 'partner'),
    )
    name = models.CharField(max_length=255)
    tier = models.CharField(max_length=255, choices=TIERS)
    website = models.CharField(max_length=255, null=True)
    twitter_handle = models.CharField(max_length=255, null=True)
    logo_filename = models.CharField(max_length=255, null=True)

    dump_dir_path = 'sponsors'
