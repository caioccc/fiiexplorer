# coding=utf-8
import logging
import requests
from bs4 import BeautifulSoup

sync_urls_delay = 30
check_new_minig_requests_delay = 86400

logger = logging.getLogger(__name__)


def dict_gen(curs):
    ''' From Python Essential Reference by David Beazley
    '''
    import itertools
    field_names = [d[0].lower() for d in curs.description]
    while True:
        rows = curs.fetchmany()
        if not rows: return
        for row in rows:
            yield dict(itertools.izip(field_names, row))


class CommonMiner():
    def get_page_bs4(self, url):
        req = requests.get(url)
        if req.status_code == 200:
            page = BeautifulSoup(req.text, 'html.parser')
            return page
        return None


class Miner(CommonMiner):
    URL = ''

    def extract(self, category):
        pass

    def get_page_url(self, url, canal, i):
        if canal == 'topcanais':
            if str(url).endswith('/'):
                return url + 'page/' + str(i)
            return str(url) + '/page/' + str(i)
        elif canal == 'canaismax':
            if 'tvaovivo' in str(url):
                return str(url)
            else:
                if str(url).endswith('/'):
                    return url + 'pag/' + str(i)
                return str(url) + '/pag/' + str(i)
        elif canal == 'filmes':
            if str(url).endswith('/'):
                return url + 'pag/' + str(i)
            return str(url) + '/pag/' + str(i)

    def mine(self):
        try:
            page = self.get_page_bs4(self.URL)
            if page:
                return True
            return False
        except (Exception,):
            return False
