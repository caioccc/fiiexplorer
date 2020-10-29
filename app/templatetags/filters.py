import datetime

from django import template

from app.views import request_json

register = template.Library()


@register.filter
def remove_text(text):
    try:
        return text
    except (Exception,):
        return ''


@register.filter(name='times')
def times(number):
    if number:
        return range(int(number))
    return None


@register.filter
def get_image(url):
    url = str(url)
    if url.startswith('/'):
        return 'https://canaismax.com' + url
    else:
        return url


@register.filter
def convert_time(strtime):
    if strtime:
        date = datetime.datetime.fromtimestamp(int(strtime))
        return "%s:%s" % (str(date.hour), str(date.minute))
    else:
        return strtime
