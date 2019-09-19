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


@register.filter
def calc_var_cota_year(list):
    try:
        vf = list[1]
        vi = list[len(list) - 1]
        res = ((float(vf.close) / float(vi.close)) - 1) * 100
        return res
    except (Exception,):
        return 0


@register.filter
def sum_dy_year(list):
    try:
        sum = 0
        for item in list:
            sum += float(item.dy)
        return float("{0:.2f}".format(sum))
    except (Exception,):
        return 0


@register.filter
def calc_median_dy(list):
    try:
        sum = 0
        for item in list:
            sum += float(item.dy)
        avg = sum / len(list)
        return float("{0:.2f}".format(avg))
    except (Exception,):
        return 0


@register.filter
def calc_median_rend(list):
    try:
        sum = 0
        for item in list:
            sum += float(item.rend)
        avg = sum / len(list)
        return float("{0:.2f}".format(avg))
    except (Exception,):
        return 0


@register.filter
def calc_median_close(list):
    try:
        sum = 0
        for item in list:
            sum += float(item.close)
        avg = sum / len(list)
        return float("{0:.2f}".format(avg))
    except (Exception,):
        return 0


@register.filter
def calc_median_osc(list):
    try:
        sum = 0
        for item in list:
            sum += float(item.rend_cota_mes)
        avg = sum / len(list)
        return float("{0:.2f}".format(avg))
    except (Exception,):
        return 0
