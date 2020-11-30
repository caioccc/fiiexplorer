# coding=utf-8
import logging
import re
import time

import requests

logging.basicConfig(level=logging.DEBUG)

from app.miner import canaismax, topcanais, filmes, series, multicanais, aovivogratis
from app.miner.common import check_new_minig_requests_delay
from app.models import Site, Serie, Channel, Filme
from app.utils import get_page_bs4, get_episodios, get_url_temporada, save_temporada, get_channel_id, \
    save_link_channel, make_ids, make_ids_topcanais, save_link_channel_multicanais, save_link_channel_topcanais, \
    make_ids_multicanais, save_url_filmes_canaismax, get_source_script_aovivogratis, get_m3u8_aovivogratis_by_eval

miners = {
    "canaismax": canaismax.CustomMiner,
    "topcanais": topcanais.CustomMiner,
    "filmes": filmes.CustomMiner,
    "series": series.CustomMiner,
    "multicanais": multicanais.CustomMiner,
    "aovivogratis": aovivogratis.CustomMiner
}

mined = 0
running = 0


def remove_iv(array_uri):
    for i in range(len(array_uri)):
        if '",IV' in str(array_uri[i]):
            index_iv = str(array_uri[i]).index('",IV=')
            if index_iv >= 0:
                array_uri[i] = str(array_uri[i])[:index_iv]
    return array_uri


def mineAllAoVivoGratis():
    while True:
        NAME = 'aovivogratis'
        site = Site.objects.get(name=NAME)
        if not site.done:
            miner = miners[NAME]()
            logging.debug('INICIOU A BUSCA AOVIVOGRATIS!')
            result = miner.mine()
            if result:
                site.done = True
                site.save()
                logging.debug('FINALIZOU A BUSCA AOVIVOGRATIS!')
                time.sleep(60)
        time.sleep(check_new_minig_requests_delay)


def snifferAoVivoGratis():
    while True:
        for ch in Channel.objects.filter(category__site__name='aovivogratis'):
            url = ch.url_site
            print('----------- sniff: ', ch.title)
            logging.debug('INICIOU A SNIFFER CANAL: ' + ch.title)
            m3u8 = get_m3u8_aovivogratis_by_eval(url)
            if m3u8:
                try:
                    link = ch.link_set.first()
                    link.m3u8 = m3u8
                    link.save()
                except (Exception,):
                    print('Nao Conseguiu atualizar o link canal ', str(ch.title))
            logging.debug('FINALIZOU SNIFFER CANAL: ' + ch.title)
            print('------------ ')
            time.sleep(3)
        time.sleep(1)


def mineSeries():
    while True:
        NAME = 'series'
        site = Site.objects.get(name=NAME)
        if not site.done:
            miner = miners[NAME]()
            logging.debug('INICIOU A BUSCA SERIES DE CANAISMAX!')
            result = miner.mine()
            if result:
                site.done = True
                site.save()
                logging.debug('FINALIZOU A BUSCA EM SERIES DE CANAISMAX!')
                time.sleep(60)
        time.sleep(check_new_minig_requests_delay)


def mineFilmes():
    while True:
        NAME = 'filmes'
        site = Site.objects.get(name=NAME)
        if not site.done:
            miner = miners[NAME]()
            logging.debug('INICIOU A BUSCA FILMES DE CANAISMAX!')
            result = miner.mine()
            if result:
                site.done = True
                site.save()
                logging.debug('FINALIZOU A BUSCA EM FILMES DE CANAISMAX!')
                time.sleep(60)
        time.sleep(check_new_minig_requests_delay)


def mineCanaisMax():
    while True:
        NAME = 'canaismax'
        site = Site.objects.get(name=NAME)
        if not site.done:
            miner = miners[NAME]()
            logging.debug('INICIOU A BUSCA EM CANAISMAX!')
            result = miner.mine()
            if result:
                site.done = True
                site.save()
                logging.debug('FINALIZOU A BUSCA EM CANAISMAX!')
                time.sleep(60)
        time.sleep(check_new_minig_requests_delay)


def mineAllTopCanais():
    while True:
        NAME = 'topcanais'
        site = Site.objects.get(name=NAME)
        if not site.done:
            miner = miners[NAME]()
            logging.debug('INICIOU A BUSCA EM TOPCANAIS!')
            result = miner.mine()
            if result:
                site.done = True
                site.save()
                logging.debug('FINALIZOU A BUSCA EM TOPCANAIS!')
                time.sleep(60)
        time.sleep(check_new_minig_requests_delay)


def mineAllMultiCanais():
    while True:
        NAME = 'multicanais'
        site = Site.objects.get(name=NAME)
        if not site.done:
            miner = miners[NAME]()
            logging.debug('INICIOU A BUSCA MULTICANAIS!')
            result = miner.mine()
            if result:
                site.done = True
                site.save()
                logging.debug('FINALIZOU A BUSCA MULTICANAIS!')
                time.sleep(60)
        time.sleep(check_new_minig_requests_delay)


def mineSeriePk(pk=None):
    while True:
        serie = Serie.objects.get(pk=pk)
        url = serie.url_site
        logging.debug('INICIOU A BUSCA SERIE: ' + url)
        temporadas = int(serie.temporadas)
        second_page = get_page_bs4(url)
        if second_page:
            temporada_obj = save_temporada(serie, 1)
            get_episodios(second_page, temporada_obj)
            if int(temporadas) > 1:
                for i_temp in range(2, (temporadas + 1)):
                    second_page_temps = get_page_bs4(get_url_temporada(url, i_temp))
                    if second_page_temps:
                        temporada_obj_temp = save_temporada(serie, int(i_temp))
                        get_episodios(second_page_temps, temporada_obj_temp)
        logging.debug('FINALIZOU A BUSCA SERIE')
        time.sleep(check_new_minig_requests_delay)


def mineChannelCanaisMax(pk=None):
    while True:
        canal = Channel.objects.get(pk=pk)
        url = canal.url_site
        logging.debug('INICIOU A BUSCA CANAISMAX CANAL: ' + url)
        second_page = get_page_bs4(url)
        if second_page:
            div_links = second_page.find_all('a', attrs={'class': 'cativ'})
            channel_id = get_channel_id(str(second_page.select('script')[-1].contents[0]))
            canal.channel_id = channel_id
            canal.save()
            if div_links:
                atags = div_links
                if len(atags) > 0:
                    ids = make_ids(atags)
                    if len(ids) > 0:
                        for id_url in ids:
                            save_link_channel(canal, id_url)
        logging.debug('FINALIZOU A BUSCA CANAISMAX DO CANAL: ' + url)
        time.sleep(check_new_minig_requests_delay)


def mineChannelTopCanais(pk=None):
    while True:
        canal = Channel.objects.get(pk=pk)
        url = canal.url_site
        logging.debug('INICIOU A BUSCA TOPCANAIS CANAL: ' + url)
        second_page = get_page_bs4(url)
        if second_page:
            div_links = second_page.find('div', attrs={'class': 'canais'})
            if div_links:
                atags = div_links.find_all("a")
                if len(atags) > 0:
                    ids = make_ids_topcanais(atags)
                    if len(ids) > 0:
                        for id_url in ids:
                            save_link_channel_topcanais(canal, id_url)
        logging.debug('FINALIZOU A BUSCA CANAISMAX DO CANAL: ' + url)
        time.sleep(check_new_minig_requests_delay)


def mineChannelMultiCanais(pk=None):
    while True:
        canal = Channel.objects.get(pk=pk)
        url = canal.url_site
        logging.debug('INICIOU A BUSCA MULTICANAIS CANAL: ' + url)
        second_page = get_page_bs4(url)
        if second_page:
            div_links = second_page.find('div', attrs={'class': 'links'})
            if div_links:
                atags = div_links.find_all("a")
                if len(atags) > 0:
                    ids = make_ids_multicanais(atags)
                    if len(ids) > 0:
                        if len(ids) == 1:
                            save_link_channel_multicanais(canal, ids[0], None)
                            save_link_channel_multicanais(canal, ids[0], 'futebolonlineaovivo.com')
                        else:
                            for id_url in ids:
                                save_link_channel_multicanais(canal, id_url, None)
        logging.debug('FINALIZOU A BUSCA MULTICANAIS CANAL: ' + url)
        time.sleep(check_new_minig_requests_delay)


def mineFilmeOneCanaisMax(pk=None):
    while True:
        filme = Filme.objects.get(pk=pk)
        url = filme.url_site
        logging.debug('INICIOU A BUSCA FILME ONE EM CANAISMAX: ' + url)
        second_page = get_page_bs4(url)
        if second_page:
            div_links = second_page.find_all('a', attrs={'class': 'cativ'})
            if div_links:
                atags = div_links
                if len(atags) > 0:
                    ids = []
                    for a in atags:
                        if a.has_attr('data-id'):
                            data_id = str(a['data-id'])
                            data_player = str(a['data-player'])
                            url_data_id = 'https://canaismax.com/embed/' + data_id + '/' + data_player
                            ids.append(url_data_id)
                    if len(ids) > 0:
                        for id_url in ids:
                            save_url_filmes_canaismax(filme, id_url)
        logging.debug('FINALIZOU A BUSCA MULTICANAIS CANAL: ' + url)
        time.sleep(check_new_minig_requests_delay)


MAX_BUFF = 3000


def contains_m3u8(page_str):
    arr_strings_without_http = list(set(remove_iv(re.findall("([^\s]+.m3u8)", page_str))))
    if len(arr_strings_without_http) > 0:
        return True, arr_strings_without_http
    return False, list(set(remove_iv(re.findall("([^\s]+.ts)", page_str))))


def is_video(type):
    if type == 'video/MP2T' or type == 'video/mp2t' or type == 'video/MP4' or \
            type == 'video/mp4' or \
            type == 'video/x-flv' or type == 'application/x-mpegURL' or \
            type == 'video/3gpp' or type == 'video/x-msvideo' or \
            type == 'video/x-ms-wmv' or type == 'video/m3u' or \
            type == 'video/m3u8' or type == 'video/hls' or type == 'vnd.apple.mpegURL':
        return True
    return False


def is_downloadable(url, headers):
    h = requests.head(url, allow_redirects=True, headers=headers)
    header = h.headers
    content_type = header.get('content-type')
    return not is_video(content_type)


def get_page_str(uri, headers):
    req = requests.get(url=uri, stream=True, headers=headers)
    type = req.headers['Content-Type']
    if req.status_code == 200:
        page_str = str(req.text)
        return page_str, type, req.status_code
    else:
        return None, None, None
