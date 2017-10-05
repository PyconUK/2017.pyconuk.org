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


class Speaker(ModelWithContent):
    name = models.CharField(max_length=255)

    dump_dir_path = 'speakers'


class Session(ModelWithContent):
    speaker = models.ForeignKey(Speaker, null=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True)
    track = models.CharField(max_length=255, null=True)
    video = models.CharField(max_length=255, null=True)
    slides = models.CharField(max_length=255, null=True)

    dump_dir_path = 'sessions'

    def session_type(self):
        return self.key.split('/', 1)[0]

    def slug(self):
        return self.key.split('/', 1)[1]

    def slot(self):
        return self.scheduleslot_set.order_by('time')[0]

    def time(self):
        return self.slot().time

    def date(self):
        return self.slot().date

    def day(self):
        return self.date().split()[0]

    def room(self):
        return self.slot().room


class ScheduleSlot(ModelWithoutContent):
    session = models.ForeignKey(Session, null=True)
    title = models.CharField(max_length=255)
    date = models.CharField(max_length=40)
    room = models.CharField(max_length=40)
    time = models.CharField(max_length=40)
    chair = models.CharField(max_length=255, null=True)

    dump_dir_path = 'schedule'


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

        # Bronze and partner sponsors appear in rows of 3
        third_tier = sponsors['bronze'] | sponsors['partner']
        while third_tier:
            yield third_tier[:3]
            third_tier = third_tier[3:]

