# -*- encoding: utf-8

from django import template

register = template.Library()


@register.filter
def colspan(row):
    # Each row in the sponsor table will have 1, 2 or 3 entries.  That means
    # there are six columns overall, which we divide up based on row length.
    if len(row) not in (1, 2, 3):
        raise ValueError("Unrecognised row length %r!" % len(row))
    return int(6 / len(row))
