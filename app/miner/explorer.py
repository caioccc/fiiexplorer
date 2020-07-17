# coding=utf-8
import logging
import time
from threading import Thread

import requests
from bs4 import BeautifulSoup

from app.miner.miner_fiis import get_info_fii
from app.models import Fundo, Site, InfoFundo
from app.miner.common import sync_urls_delay, check_new_minig_requests_delay
from app.miner import fundsexplorer

readers = {
    "fundsexplorer": fundsexplorer.CustomReader
}

miners = {
    "fundsexplorer": fundsexplorer.CustomMiner
}

mined = 0
running = 0


def syncFunds():
    settings = Settings.getInstance()
    while True:
        funds = Fundo.objects.all()
        for fund in funds:
            customreader = readers["fundsexplorer"]()
            logging.debug('---- Fundo Reader:' + fund.sigla)
            customreader.sync(fund)
            settings.count_mined(fund, len(funds))
            time.sleep(5)
        settings.set_mined(0)
        time.sleep(sync_urls_delay)


def getInfos():
    InfoFundo.objects.all().delete()
    fundos = Fundo.objects.all()
    for fundo in fundos:
        if len(fundo.infofundo_set.all()) == 0:
            print('Buscando ... Info Fundo: ' + fundo.sigla)
            table = get_info_fii(fundo.sigla)
            if table:
                for i in range(0, len(table)):
                    info = InfoFundo()
                    info.fund = fundo
                    info.dy = table[i][3]
                    info.data_pay = table[i][1]
                    info.data_base = table[i][0]
                    info.close = table[i][2]
                    info.rend = table[i][4]
                    info.rend_cota_mes = table[i][5]
                    info.save()
                print('Saved info to: ', fundo.sigla)
        time.sleep(1)


def mineData():
    while True:
        sites = Site.objects.filter(done=False)
        for site in sites:
            domain = site.nome
            miner = miners[domain]()
            logging.debug('INICIOU A BUSCA!')
            result = miner.mine()
            if result:
                site.done = True
                site.save()
                logging.debug('FINALIZOU A BUSCA!')
                time.sleep(60)
        time.sleep(check_new_minig_requests_delay)


class Settings():
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Settings.__instance == None:
            Settings()
        return Settings.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Settings.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Settings.__instance = self

    mined = 0
    running = False
    thread = Thread(target=syncFunds)
    minerThread = Thread(target=mineData)
    infosThread = Thread(target=getInfos)

    def set_running(self, val):
        self.running = val

    def get_running(self):
        return self.running

    def get_mined(self):
        return self.mined

    def set_mined(self, mined=0):
        self.mined = mined

    def count_mined(self, fund, total):
        if fund:
            self.mined = self.mined + 1
            return float(self.mined) / float(total)
        else:
            return float(self.mined) / float(total)
