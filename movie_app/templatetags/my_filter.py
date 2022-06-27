from django import template
from django.db.models import QuerySet

register = template.Library()


@register.filter(name='cut')
def cut_filter(arg, *args):
    return arg[args]


@register.filter(name='list')
def list_filter(arg: QuerySet):
    return arg[:]
