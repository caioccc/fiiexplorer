import requests
from bs4 import BeautifulSoup

DY_TEXT = 'Rendimento no valor de R$ '
DATA_PAY_TEXT = 'por cota no dia '
DATA_BASE_TEXT = 'Data base: '
CLOSE_TEXT = 'Fechamento: R$ '
RENDIMENTO_TEXT = 'Rendimento%: '


def get_infos(content):
    split_dy = str(content.text).split(DY_TEXT)
    split_data_pay = str(content.text).split(DATA_PAY_TEXT)
    split_data_base = str(content.text).split(DATA_BASE_TEXT)
    split_close = str(content.text).split(CLOSE_TEXT)
    split_rend = str(content.text).split(RENDIMENTO_TEXT)
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
        dy.append(float(a[0:9]))
    for b in split_data_pay:
        data_pay.append(b[0:10])
    for c in split_data_base:
        data_base.append(c[0:10])
    for d in split_close:
        close.append(float(d[0:6]))
    for e in split_rend:
        rend.append(float(e[0:4]))
    if len(close) > 0:
        for i in range(0, len(close)):
            if i == 0:
                rend_cota_mes.append(0.00)
            else:
                vf = close[i]
                vi = close[i - 1]
                rm = ((vf / vi) - 1) * 100
                rend_cota_mes.append(rm)

    return dy, data_pay, data_base, close, rend, rend_cota_mes


def get_info_fii(sigla):
    req = requests.get('https://fiis.com.br/' + sigla)
    if req.status_code == 200:
        page = BeautifulSoup(req.text, 'html.parser')
        div_entry_content = page.find('div', {'class': 'entry-content'})
        dy, data_pay, data_base, close, rend, rend_cota_mes = get_infos(div_entry_content)
        return dy, data_pay, data_base, close, rend, rend_cota_mes
    else:
        return None
