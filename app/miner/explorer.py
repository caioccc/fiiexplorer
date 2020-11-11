# coding=utf-8
import logging
import re
import time

import requests

from app.miner import canaismax, topcanais, filmes, series, multicanais
from app.miner.common import check_new_minig_requests_delay
from app.models import Site, Serie, Channel, Link
from app.utils import get_page_bs4, get_episodios, get_url_temporada, save_temporada, get_channel_id, \
    save_link_channel, make_ids, get_headers, make_ids_topcanais, save_link_channel_multicanais
from fiiexplorer.settings import SITE_URL

miners = {
    "canaismax": canaismax.CustomMiner,
    "topcanais": topcanais.CustomMiner,
    "filmes": filmes.CustomMiner,
    "series": series.CustomMiner,
    "multicanais": multicanais.CustomMiner,
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


def mineSeries():
    while True:
        NAME = 'series'
        site = Site.objects.get(name=NAME)
        if not site.done:
            miner = miners[NAME]()
            logging.debug('INICIOU A BUSCA SERIES CANAISMAX!')
            result = miner.mine()
            if result:
                site.done = True
                site.save()
                logging.debug('FINALIZOU A BUSCA EM SERIES CANAISMAX!')
                time.sleep(60)
        time.sleep(check_new_minig_requests_delay)


def mineFilmes():
    while True:
        NAME = 'filmes'
        site = Site.objects.get(name=NAME)
        if not site.done:
            miner = miners[NAME]()
            logging.debug('INICIOU A BUSCA FILMES CANAISMAX!')
            result = miner.mine()
            if result:
                site.done = True
                site.save()
                logging.debug('FINALIZOU A BUSCA EM FILMES CANAISMAX!')
                time.sleep(60)
        time.sleep(check_new_minig_requests_delay)


def mineCanaisMax():
    while True:
        NAME = 'canaismax'
        site = Site.objects.get(name=NAME)
        if not site.done:
            miner = miners[NAME]()
            logging.debug('INICIOU A BUSCA CANAISMAX!')
            result = miner.mine()
            if result:
                site.done = True
                site.save()
                logging.debug('FINALIZOU A BUSCA EM CANAISMAX!')
                time.sleep(60)
        time.sleep(check_new_minig_requests_delay)


def mineTopCanais():
    while True:
        NAME = 'topcanais'
        site = Site.objects.get(name=NAME)
        if not site.done:
            miner = miners[NAME]()
            logging.debug('INICIOU A BUSCA TOPCANAIS!')
            result = miner.mine()
            if result:
                site.done = True
                site.save()
                logging.debug('FINALIZOU A BUSCA TOPCANAIS!')
                time.sleep(60)
        time.sleep(check_new_minig_requests_delay)


def mineMultiCanais():
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


def mineCanalPk(pk=None):
    while True:
        canal = Channel.objects.get(pk=pk)
        url = canal.url_site
        logging.debug('INICIOU A BUSCA CANAL: ' + url)
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
        logging.debug('FINALIZOU A BUSCA CANAL')
        time.sleep(check_new_minig_requests_delay)


def mineCanalMultiCanais(pk=None):
    while True:
        canal = Channel.objects.get(pk=pk)
        url = canal.url_site
        logging.debug('INICIOU A BUSCA CANAL: ' + url)
        second_page = get_page_bs4(url)
        if second_page:
            div_links = second_page.find('div', attrs={'class': 'links'})
            if div_links:
                atags = div_links.find_all("a")
                if len(atags) > 0:
                    ids = make_ids_topcanais(atags)
                    if len(ids) > 0:
                        for id_url in ids:
                            save_link_channel_multicanais(canal, id_url)
        logging.debug('FINALIZOU A BUSCA CANAL')
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


def is_downloadable(url):
    h = requests.head(url, allow_redirects=True, headers=get_headers())
    header = h.headers
    content_type = header.get('content-type')
    return not is_video(content_type)


def get_page_str(uri):
    req = requests.get(url=uri, stream=True, headers=get_headers())
    type = req.headers['Content-Type']
    if req.status_code == 200:
        page_str = str(req.text)
        return page_str, type, req.status_code
    else:
        return None, None, None
