from django import template

register = template.Library()


@register.filter
def remove_text(text):
    try:
        return text.replace('is greater than or equal to', '').replace('is less than or equal to', '').replace(
            'contains', '')
    except (Exception,):
        return ''


@register.filter
def ispositive(text):
    try:
        return float(text) >= float(0)
    except (Exception,):
        return False
