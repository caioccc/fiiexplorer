# coding: UTF-8
import requests
from bs4 import BeautifulSoup

DY_TEXT = 'Rendimento no valor de R$ '
DATA_PAY_TEXT = 'por cota no dia '
DATA_BASE_TEXT = 'Data base: '
CLOSE_TEXT = 'Fechamento: R$ '
RENDIMENTO_TEXT = 'Rendimento%: '


def get_infos(table):
    closes = []
    for item in table:
        if str(item[2]).count('.') == 1:
            closes.append(float(str(item[2]).replace('R$ ', '').replace('.', '').replace(',', '.')))
        else:
            closes.append(float(str(item[2]).replace('R$ ', '').replace(',', '.')))
    rends = []
    for i in range(0, len(closes)):
        if i == len(closes) - 1:
            rm = 0.00
        elif i < len(closes) - 1:
            vf = closes[i]
            vi = closes[i + 1]
            rm = ((vf / vi) - 1) * 100
        rends.append(float("{:.2f}".format(rm)))
    new_table = []
    for k in range(0, len(table)):
        if str(table[k][2]).count('.') == 1:
            close = float(str(table[k][2]).replace('R$ ', '').replace('.', '').replace(',', '.'))
        else:
            close = float(str(table[k][2]).replace('R$ ', '').replace(',', '.'))
        new_table.append(
            [
                table[k][0],
                table[k][1],
                close,
                float(str(table[k][3]).replace('%', '').replace(',', '.')),
                float(str(table[k][4]).replace('R$ ', '').replace(',', '.')),
                rends[k]
            ]
        )
    return new_table


def get_info_fii(sigla):
    req = requests.get('https://fiis.com.br/' + sigla)
    if req.status_code == 200:
        page = BeautifulSoup(req.text, 'html.parser')
        div_entry_content = page.find('table')
        data = []
        table_body = div_entry_content.find('tbody')
        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])
        return get_infos(data)
    else:
        return None
