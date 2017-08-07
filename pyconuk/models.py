import datetime
import re

from django.db import models
from django_amber.models import ModelWithContent, ModelWithoutContent


class Page(ModelWithContent):
    title = models.CharField(max_length=100)
    template = models.CharField(max_length=20, default='page.html')

    dump_dir_path = 'pages'
