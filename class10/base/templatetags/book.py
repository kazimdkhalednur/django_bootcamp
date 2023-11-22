from django import template
from base.models import Book

register = template.Library()

@register.filter
def count():
    count = Book.objects.count()
    return count