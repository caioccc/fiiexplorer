# coding=utf-8
import time

from app.models import Fundo
from common import sync_urls_delay, check_new_minig_requests_delay
from app.miner import fundsexplorer

readers = {
    "fundsexplorer": fundsexplorer.CustomReader
}

miners = {
    "fundsexplorer": fundsexplorer.CustomMiner
}


def syncFunds():
    while True:
        funds = Fundo.objects.all()
        for fund in funds:
            customreader = readers["fundsexplorer"]()
            customreader.sync(fund)
            time.sleep(500)
        time.sleep(sync_urls_delay)


def mineData():
    while True:
        miner = miners["fundsexplorer"]()
        minery = miner.mine()
        if minery:
            time.sleep(60)

        time.sleep(check_new_minig_requests_delay)
