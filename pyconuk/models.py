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

    @classmethod
    def sponsors_by_tier(cls):
        return {
            tier: Sponsor.objects.filter(tier=tier)
            for _, tier in Sponsor.TIERS
        }

    @classmethod
    def sponsor_rows(cls):
        sponsors = cls.sponsors_by_tier()

        # Gold sponsors get their own row
        for s in sponsors['gold']:
            yield [s]

        # Silver sponsors appear in rows of 2 or 3
        while True:
            if len(sponsors['silver']) >= 4:
                yield sponsors['silver'][:2]
                sponsors['silver'] = sponsors['sponsors'][2:]
            else:
                yield sponsors['silver']
                break

        # Bronze and partner sponsors appear in rows of 3j
        third_tier = sponsors['bronze'] | sponsors['partner']
        while third_tier:
            yield third_tier[:3]
            third_tier = third_tier[3:]

