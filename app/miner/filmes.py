from app.miner.common import Miner
from app.models import Channel, Link, Site, Filme, Url


class CustomMiner(Miner):

    def extract(self, category):
        pages = int(category.pages) + 1
        for i in range(1, pages):
            temp_url = self.get_page_url(category.url, 'filmes', i)
            page = self.get_page_bs4(temp_url)
            if page:
                divs_entries = page.select('div.item')
                print('total_canais', len(divs_entries))
                if len(divs_entries) > 0:
                    for div in divs_entries:
                        atag = div.find('a')
                        href = atag['href']
                        array_temp = [text for text in atag.find('span', {'class': 'name'}).stripped_strings]
                        title = str(array_temp[0])
                        ano = str(array_temp[1])
                        duracao = str(array_temp[2])
                        imdb = str(array_temp[3])
                        if len(array_temp) == 5:
                            tipo = str(array_temp[4])
                        else:
                            tipo = str(str(array_temp[4]) + '/' + str(array_temp[5]))
                        img_tag = atag.find('img')
                        if img_tag.has_attr('src'):
                            img_url = img_tag['src']
                        elif img_tag.has_attr('data-src'):
                            img_url = img_tag['data-src']
                        else:
                            img_url = ''
                        second_page = self.get_page_bs4(href)
                        if second_page:
                            sinopse = '' if len(second_page.select('section.description')) == 0 else \
                                second_page.select('section.description')[0].get_text()
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
                                        self.save_filme(ano, category, duracao, ids, imdb, img_url, sinopse, tipo,
                                                        title)

    def save_filme(self, ano, category, duracao, ids, imdb, img_url, sinopse, tipo, title):
        ch = Filme()
        ch.ano = ano
        ch.sinopse = sinopse
        ch.duracao = duracao
        ch.title = (title[:230] + '..') if len(title) > 75 else title
        ch.img_url = img_url
        ch.category = category
        ch.imdb = imdb
        ch.tipo = tipo
        ch.save()
        for id_url in ids:
            link = Url()
            link.url = id_url
            link.filme = ch
            link.save()

    def mine(self):
        try:
            Filme.objects.all().delete()
            Url.objects.all().delete()
            site = Site.objects.get(name='filmes')
            for category in site.categorychannel_set.all():
                self.extract(category)
            return True
        except (Exception,):
            return False
