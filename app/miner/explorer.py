# coding=utf-8
import logging
import time

from app.miner import canaismax, topcanais, filmes, series
from app.miner.common import check_new_minig_requests_delay
from app.utils import get_page_bs4, get_episodios, get_url_temporada, save_temporada, get_channel_id, \
    save_link_channel, make_ids
from app.models import Site, Serie, Channel

miners = {
    "canaismax": canaismax.CustomMiner,
    "topcanais": topcanais.CustomMiner,
    "filmes": filmes.CustomMiner,
    "series": series.CustomMiner
}

mined = 0
running = 0


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
