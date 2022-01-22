from django import template
from ..models import SchoolNews


register = template.Library()


@register.simple_tag
def total_news():
    return SchoolNews.objects.count()
