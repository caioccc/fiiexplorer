# coding=utf-8
import logging
import time
from threading import Thread

from app.miner import canaismax, topcanais, filmes, series
from app.miner.common import sync_urls_delay, check_new_minig_requests_delay
from app.models import Site

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
