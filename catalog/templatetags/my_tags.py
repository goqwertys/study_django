from django import template

from config import settings

register = template.Library()

@register.filter()
def media_filter(image_field):
    if image_field and hasattr(image_field, 'url'):
        return image_field.url
    else:
        return '#'
