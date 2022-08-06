from django import template
from datetime import datetime

register = template.Library()

@register.simple_tag()
def my_time(format_string='%b %d %Y'):
    return datetime.utcnow().strftime(format_string)