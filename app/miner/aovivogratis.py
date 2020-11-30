import re

from app.miner.common import Miner
from app.models import Channel, Link, Site
from app.utils import get_page_bs4, get_source_script_aovivogratis, save_link_channel_aovivogratis, clean_title


def get_title(href):
    href = str(href)
    index_bar = href.rfind('/')
    index_end = href.rfind('.')
    return href[index_bar + 1:index_end]


def exists_title_in_multicanais(title):
    if 'telecine' in title.lower():
        return False
    if 'hbo' in title.lower():
        return False
    if 'max' in title.lower():
        return False
    lista = [clean_title(ch) for ch in Channel.objects.filter(category__site__name='multicanais')]
    li = [titulo for titulo in lista if re.search(titulo, title.lower(), re.IGNORECASE)]
    if len(li) > 0:
        return True
    return False


class CustomMiner(Miner):

    def extract(self, category):
        pages = int(category.pages) + 1
        for i in range(1, pages):
            temp_url = category.url
            page = get_page_bs4(temp_url)
            if page:
                divs_entries = page.select('div.post-thumb-img-content')
                if len(divs_entries) > 0:
                    divs_entries = divs_entries[:154]
                    for div in divs_entries:
                        atag = div.find('a')
                        href = atag['href']
                        imgtag = atag.find('img')
                        title = imgtag['alt']
                        img_url = imgtag['data-src']
                        if title == '':
                            title = get_title(img_url)
                        if not exists_title_in_multicanais(title):
                            second_page = get_page_bs4(href)
                            if second_page:
                                div_links = second_page.find('iframe')
                                if div_links:
                                    ids = self.make_ids_multicanais(div_links)
                                    if ids:
                                        ids = ids.replace('external', '')
                                        m3u8 = get_source_script_aovivogratis(ids)
                                        if m3u8:
                                            ch = Channel()
                                            ch.title = title
                                            ch.img_url = img_url
                                            ch.category = category
                                            ch.url_site = str(ids)
                                            ch.save()
                                            print(title, )
                                            save_link_channel_aovivogratis(ch, href, m3u8)

    def make_ids_multicanais(self, div_links):
        return div_links['data-src']

    def mine(self):
        Channel.objects.filter(category__site__name='aovivogratis').delete()
        Link.objects.filter(channel__category__site__name='aovivogratis').delete()
        site = Site.objects.get(name='aovivogratis')
        for category in site.categorychannel_set.all():
            self.extract(category)
        return True
