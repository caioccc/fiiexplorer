import datetime

from django import template

from app.utils import check_m3u8_req

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
def is_m3u8_valid(link):
    headers = {'origin': 'https://futemax.live', 'referer': 'https://futemax.live/'}
    return check_m3u8_req(link['m3u8'], headers=headers)


@register.filter
def get_text_type_futemax(link):
    uri = str(link['m3u8'])
    if 'sd/' in uri:
        return 'SD'
    elif 'hd/' in uri:
        return 'HD'
    else:
        return ''


@register.filter
def get_text_type(link):
    uri = str(link.m3u8)
    if 'sd/' in uri:
        return 'SD'
    elif 'hd/' in uri:
        return 'HD'
    else:
        return ''


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
