import re

import m3u8
import requests
from bs4 import BeautifulSoup

from app.models import Episodio, LinkSerie, Temporada, Link


def get_page_bs4(url):
    req = requests.get(url)
    if req.status_code == 200:
        page = BeautifulSoup(req.text, 'html.parser')
        return page
    return None


def get_episodios(page, temporada):
    section = page.find('section', {'class': 'temporadas-grid'})
    divs_episodios = section.select('div.item')
    print('total_episodios', len(divs_episodios))
    if len(divs_episodios) > 0:
        for div_ep in divs_episodios:
            atag_episodio = div_ep.find('a')
            href_episodio = atag_episodio['href']
            img_tag_episodio = atag_episodio.find('img')
            img_url_episodio = get_img_url(img_tag_episodio)
            array_episodio_temp = [text for text in atag_episodio.find('span', {
                'class': 'info'}).stripped_strings]
            if len(array_episodio_temp) == 2:
                type_episodio = array_episodio_temp[0]
                title_episodio = array_episodio_temp[1]
            else:
                type_episodio = array_episodio_temp[0]
                title_episodio = ''
            third_page = get_page_bs4(href_episodio)
            if third_page:
                div_links_epi = third_page.find_all('a', attrs={'class': 'cativ'})
                if div_links_epi:
                    atag_ep_link = div_links_epi
                    if len(atag_ep_link) > 0:
                        ids = []
                        for a_url_epi in atag_ep_link:
                            if a_url_epi.has_attr('data-id'):
                                data_id = str(a_url_epi['data-id'])
                                data_episodio = str(a_url_epi['data-episodio'])
                                data_player = str(a_url_epi['data-player'])
                                url_data_id = 'https://canaismax.com/embed/' + data_id + '/' + data_episodio + '/' + data_player
                                ids.append(url_data_id)
                        if len(ids) > 0:
                            save_episodio(ids, img_url_episodio, title_episodio, type_episodio, temporada)


def save_episodio(ids, img_url_episodio, title_episodio, type_episodio, temporada):
    episodio = Episodio()
    episodio.temporada = temporada
    episodio.img_url = img_url_episodio
    episodio.type = type_episodio
    episodio.title = title_episodio
    episodio.save()
    for id_url_epi in ids:
        link = LinkSerie()
        link.url = id_url_epi
        link.episodio = episodio
        link.save()


def get_img_url(img_tag):
    if img_tag.has_attr('src'):
        img_url = img_tag['src']
    elif img_tag.has_attr('data-src'):
        img_url = img_tag['data-src']
    else:
        img_url = ''
    return img_url


def get_url_temporada(url, i):
    if str(url).endswith('/'):
        return url + 'temporada/' + str(i)
    return str(url) + '/temporada/' + str(i)


def save_temporada(serie, num_seq):
    temporada_obj = Temporada()
    temporada_obj.num_seq = num_seq
    temporada_obj.serie = serie
    temporada_obj.save()
    return temporada_obj


def get_channel_id(string_script):
    api_url = 'https://canaismax.com/api/canal/'
    if api_url in string_script:
        ind = string_script.index(api_url) + len(api_url)
        ind_bar = ind + 24
        id = string_script[ind:ind_bar]
        return id
    return ''


def save_link_channel(canal, id_url):
    # link = Link()
    # link.url = id_url
    # link.channel = canal
    # link.m3u8 = get_m3u8(id_url)
    # link.save()
    # if link.m3u8 and link.m3u8 != '':
    #     save_tss(link.m3u8, canal.title, canal.img_url, link)
    # else:
    #     print(canal.title, 'nao tem .m3u8')
    link = Link()
    link.url = id_url
    link.channel = canal
    link.m3u8 = get_m3u8(id_url)
    link.save()


def get_headers():
    headers = {'origin': 'https://canaismax.com', 'referer': 'https://canaismax.com/'}
    return headers


def contain_http(uri):
    if str(uri).startswith('http'):
        return True
    return False


# def save_tss(uri, name, logo, link):
#     headers = get_headers()
#     if uri != '':
#         try:
#             if contain_http(uri):
#                 req = requests.get(url=uri, headers=headers)
#                 if req.status_code == 200:
#                     page = BeautifulSoup(req.text, 'html.parser')
#                     page_str = str(page.contents[0])
#                     arr_strings = re.findall("(?P<url>https?://[^\s]+)", page_str)
#                     if len(arr_strings) > 0:
#                         for ts_uri in arr_strings:
#                             _save_ts(headers, link, logo, name, ts_uri)
#                     else:
#                         arr_strings = re.findall("([^\s]+.m3u8)", page_str)
#                         for ts_uri in arr_strings:
#                             print(ts_uri, 'nao foi possivel salvar TS')
#                             # _save_ts(headers, link, logo, name, ts_uri)
#             else:
#                 print('nao contem http ', uri)
#         except(requests.exceptions.ConnectionError,):
#             print(link.channel.title, 'nao foi possivel salvar TS')
#         except (Exception,):
#             print(link.channel.title, 'nao foi possivel salvar TS')
#
#
# def _save_ts(headers, link, logo, name, ts_uri):
#     try:
#         if contain_http(ts_uri):
#             req_test_uri = requests.get(url=ts_uri, stream=True, headers=headers)
#             if req_test_uri.status_code == 200:
#                 ts = Ts(link=link, name=name, logo=logo, uri=ts_uri)
#                 ts.save()
#         else:
#             print('TS not contain https ', ts_uri)
#     except (requests.exceptions.ConnectionError,):
#         print('Connection Error', link.channel.title)


def get_m3u8(id_url):
    try:
        miner_req = get_page_bs4(id_url)
        if miner_req:
            script = None
            for scr in miner_req.select('script'):
                if len(scr.contents) > 0:
                    if 'document.referrer' in str(scr.contents[0]):
                        script = scr
            content_script = str(script.contents[0])
            string_source = 'source: "'
            string_m3u8 = '.m3u8'
            sources_indexes = [m.start() for m in
                               re.finditer(string_source, content_script)]
            m3u8_indexes = [m.start() for m in
                            re.finditer(string_m3u8, content_script)]
            strings = [
                content_script[(int(sources_indexes[i]) + len(string_source)):(int(m3u8_indexes[i]) + len(string_m3u8))]
                for i in range(len(sources_indexes))]
            if len(strings) > 0:
                return strings[0]
            return ''
    except (Exception,):
        return ''


def make_ids(atags):
    ids = []
    for a in atags:
        if a.has_attr('data-link'):
            data_id = str(a['data-link'])
            if 'op=' in data_id:
                third_page_temp = get_page_bs4(data_id)
                if third_page_temp:
                    div_buttons = third_page_temp.find('div',
                                                       attrs={
                                                           'class': 'buttons-quality'})
                    if div_buttons:
                        novos_links = div_buttons.find_all('a')
                        if len(novos_links) > 0:
                            for alinks_temp in novos_links:
                                if alinks_temp.has_attr('href'):
                                    alink_temp_url = str(alinks_temp['href'])
                                    ids.append(alink_temp_url)
            else:
                ids.append(data_id)
    return ids
