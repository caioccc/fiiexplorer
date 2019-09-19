# coding: UTF-8
import requests
from bs4 import BeautifulSoup

DY_TEXT = 'Rendimento no valor de R$ '
DATA_PAY_TEXT = 'por cota no dia '
DATA_BASE_TEXT = 'Data base: '
CLOSE_TEXT = 'Fechamento: R$ '
RENDIMENTO_TEXT = 'Rendimento%: '


def get_infos(content):
    split_dy = content.split(DY_TEXT)
    split_data_pay = content.split(DATA_PAY_TEXT)
    split_data_base = content.split(DATA_BASE_TEXT)
    split_close = content.split(CLOSE_TEXT)
    split_rend = content.split(RENDIMENTO_TEXT)
    split_dy = split_dy[1:]
    split_data_pay = split_data_pay[1:]
    split_data_base = split_data_base[1:]
    split_close = split_close[1:]
    split_rend = split_rend[1:]
    dy = []
    data_pay = []
    data_base = []
    close = []
    rend = []
    rend_cota_mes = []
    for a in split_dy:
        if ('p' in a[0:4]):
            dy.append(float(a[0:1]))
        else:
            dy.append(float(a[0:4].replace(',', '.')))
    for b in split_data_pay:
        data_pay.append(b[0:10])
    for c in split_data_base:
        data_base.append(c[0:10])
    for d in split_close:
        if 'R' in d[0:4] or 'r' in d[0:4]:
            close.append(float(d[0:2]))
        else:
            close.append(float(d[0:4].replace(',', '.')))
    for e in split_rend:
        rend.append(float(e[0:4].replace(',', '.')))
    if len(close) > 0:
        for i in range(0, len(close)):
            if i == (len(close)-1):
                rend_cota_mes.append(0.00)
            else:
                vf = close[i]
                vi = close[i + 1]
                rm = ((vf / vi) - 1) * 100
                rend_cota_mes.append(rm)

    return dy, data_pay, data_base, close, rend, rend_cota_mes


def get_info_fii(sigla):
    req = requests.get('https://fiis.com.br/' + sigla)
    if req.status_code == 200:
        page = BeautifulSoup(req.text, 'html.parser')
        div_entry_content = page.find('div', {'class': 'entry-content'}).text
        dy, data_pay, data_base, close, rend, rend_cota_mes = get_infos(div_entry_content)
        return dy, data_pay, data_base, close, rend, rend_cota_mes
    else:
        return None
