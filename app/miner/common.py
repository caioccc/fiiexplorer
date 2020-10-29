# coding=utf-8
import logging

from app.utils import get_page_bs4

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


class Miner():
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
        elif canal == 'filmes' or canal == 'series':
            if i > 1:
                if str(url).endswith('/'):
                    return url + 'pag/' + str(i)
                return str(url) + '/pag/' + str(i)
            else:
                return str(url)

    def mine(self):
        pass
