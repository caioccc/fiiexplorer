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
        vf = list[0]
        vi = list[len(list) - 1]
        res = ((float(vf.close) / float(vi.close)) - 1) * 100
        return res
    except (Exception,):
        return 0


@register.filter
def calc_var_cota_by_month(list, month):
    try:
        vf = list[0]
        vi = list[int(month)]
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


@register.filter
def show_formated_float(numb):
    if numb:
        numb = round(float(numb), 2)
        return '%.2f' % numb
    else:
        return None


def get_osc_by_month_fut(fundo, month):
    lista = fundo.infofundo_set.all()
    arr = []
    if len(lista) >= 12:
        lista = lista[:12]
        for i in lista:
            arr.append(i.rend_cota_mes)
    arr = arr[::-1]
    return arr[month]


def get_dy_percent_by_month_fut(fundo, month):
    lista = fundo.infofundo_set.all()
    arr = []
    if len(lista) >= 12:
        lista = lista[:12]
        for i in lista:
            arr.append(i.rend)
    arr = arr[::-1]
    return arr[month]


def calc_value_by_percent(val_total, percent):
    return float(val_total) * float(float(percent) / 100)


@register.filter
def make_map(fundo):
    mapa = []
    lista = fundo.infofundo_set.all()
    if len(lista) >= 12:
        lista = lista[:12]
        next = lista[0].close
        for i in range(0, len(lista)):
            percent_dy = get_dy_percent_by_month_fut(fundo, i)
            osc = get_osc_by_month_fut(fundo, i)
            mapa.append([next, osc, percent_dy,
                         str(calc_value_by_percent(next, percent_dy))])
            next = str(((float(osc) / 100) + 1) * float(next))
    else:
        print('Existe menos de 12 registros para o fundo: ', fundo.sigla)
    return mapa


def val_total_fundo_investido(fundo, qtd=1):
    mapa = make_map(fundo)
    soma = 0
    for i in range(len(mapa)):
        soma = float(soma) + (float(mapa[i][0]) * float(qtd))
    return soma


@register.filter
def valor_total_investido(carteira):
    soma = 0
    for itemfundo in carteira.itemfundo_set.all():
        val_total_investido_fundo = val_total_fundo_investido(itemfundo.fundo, itemfundo.qtd)
        soma = float(soma) + float(val_total_investido_fundo)
    return soma


@register.filter
def valorizacao_patrimonial_carteira(carteira):
    valores_totais_fundos = 0
    for itemfundo in carteira.itemfundo_set.all():
        mapa_fundo = make_map(itemfundo.fundo)
        xclose11 = mapa_fundo[-1][0]
        valor_total_fundo_atual = float(xclose11) * (float(itemfundo.qtd) * float(12))
        valores_totais_fundos = float(valores_totais_fundos) + valor_total_fundo_atual
    return valores_totais_fundos


@register.filter
def rendimentos_totais_carteira(carteira):
    soma_dy = 0
    for itemfundo in carteira.itemfundo_set.all():
        mapa_fundo = make_map(itemfundo.fundo)
        for i in range(len(mapa_fundo)):
            soma_dy = float(soma_dy) + (float(mapa_fundo[i][3]) * (float(itemfundo.qtd) * float(i + 1)))
    return soma_dy


@register.filter
def montante_final_carteira(carteira):
    valorizacao = valorizacao_patrimonial_carteira(carteira)
    rend = rendimentos_totais_carteira(carteira)
    return float(valorizacao) + float(rend)


@register.filter()
def ranger(min=3):
    return range(1, min + 1)


@register.filter()
def get_valor_investido(carteira, month):
    val_investido = 0
    for itemfundo in carteira.itemfundo_set.all():
        mapa_fundo = make_map(itemfundo.fundo)[:(month)]
        for i in range(len(mapa_fundo)):
            val_investido = float(val_investido) + float(float(mapa_fundo[i][0]) * float(itemfundo.qtd))
    return val_investido


@register.filter()
def get_valor_patrimonial(carteira, month):
    vp = 0
    for itemfundo in carteira.itemfundo_set.all():
        mapa_fundo = make_map(itemfundo.fundo)[:(month)]
        vp = float(vp) + (float(mapa_fundo[month - 1][0]) * (float(itemfundo.qtd) * float(month)))
    return vp


@register.filter()
def get_rendimento_month(carteira, month):
    rend = 0
    for itemfundo in carteira.itemfundo_set.all():
        mapa_fundo = make_map(itemfundo.fundo)[:(month)]
        rend = float(rend) + (float(mapa_fundo[month - 1][3]) * (float(itemfundo.qtd) * float(month)))
    return rend


@register.filter()
def get_rendimento(carteira, month):
    suma = float(0)
    if month > 1:
        for i in range(month):
            suma += get_rendimento_month(carteira, month-i)
        return suma
    else:
        return get_rendimento_month(carteira, month)


@register.filter()
def get_montante_final(carteira, month):
    return get_valor_patrimonial(carteira, month) + get_rendimento(carteira, month)
