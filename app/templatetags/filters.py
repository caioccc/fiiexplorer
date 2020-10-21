from django import template

register = template.Library()


@register.filter
def remove_text(text):
    try:
        return text
    except (Exception,):
        return ''

