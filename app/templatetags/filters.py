import datetime

from django import template

register = template.Library()


@register.filter
def remove_text(text):
    try:
        return text
    except (Exception,):
        return ''


@register.filter
def convert_time(strtime):
    if strtime:
        date = datetime.datetime.fromtimestamp(int(strtime))
        return "%s:%s" % (str(date.hour), str(date.minute))
    else:
        return strtime
