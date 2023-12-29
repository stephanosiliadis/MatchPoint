from django import template
from django.template.defaulttags import register


register = template.Library()


@register.filter
def make_list(value):
    return range(1, value + 1)


@register.filter
def to_int(value):
    return int(value)
