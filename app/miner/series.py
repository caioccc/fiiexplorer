from app.miner.common import Miner
from app.models import Channel, Link, Site, Serie, Episodio, LinkSerie, Temporada


class CustomMiner(Miner):

    def get_url_temporada(self, url, i):
        if str(url).endswith('/'):
            return url + 'temporada/' + str(i)
        return str(url) + '/temporada/' + str(i)

    def extract(self, category):
        pages = int(category.pages) + 1
        for i in range(1, pages):
            temp_url = self.get_page_url(category.url, 'series', i)
            page = self.get_page_bs4(temp_url)
            if page:
                divs_entries = page.select('div.item')
                print('total_series', len(divs_entries))
                if len(divs_entries) > 0:
                    for div in divs_entries:
                        atag = div.find('a')
                        href = atag['href']
                        array_temp = [text for text in atag.find('span', {'class': 'name'}).stripped_strings]
                        title = str(array_temp[0])
                        temporadas = self.get_temporadas(str(array_temp[2]))
                        imdb = str(array_temp[3])
                        if len(array_temp) == 5:
                            tipo = str(array_temp[4])
                        else:
                            tipo = str(str(array_temp[4]) + '/' + str(array_temp[5]))
                        img_tag = atag.find('img')
                        img_url = self.get_img_url(img_tag)
                        second_page = self.get_page_bs4(href)
                        if second_page:
                            sinopse = '' if len(second_page.select('section.description')) == 0 else \
                                second_page.select('section.description')[0].get_text()
                            array_temp_details = [text for text in second_page.find('section', {
                                'class': 'details-filme'}).stripped_strings]
                            episodios = str(array_temp_details[0])
                            duracao = str(array_temp_details[1])
                            ano = str(array_temp_details[2])
                            serie = self.save_serie(ano, duracao, episodios, imdb, img_url, sinopse, temporadas, tipo,
                                                    title)
                            temporada_obj = Temporada()
                            temporada_obj.num_seq = 1
                            temporada_obj.serie = serie
                            temporada_obj.save()
                            self.get_episodios(second_page, temporada_obj)
                            if int(temporadas) > 1:
                                for i_temp in range(2, (int(temporadas) + 1)):
                                    second_page_temps = self.get_page_bs4(self.get_url_temporada(href, i_temp))
                                    if second_page_temps:
                                        temporada_obj_temp = Temporada()
                                        temporada_obj_temp.num_seq = int(i_temp)
                                        temporada_obj_temp.serie = serie
                                        temporada_obj_temp.save()
                                        self.get_episodios(second_page_temps, temporada_obj)

    def get_episodios(self, page, temporada):
        section = page.find('section', {'class': 'temporadas-grid'})
        divs_episodios = section.select('div.item')
        print('total_episodios', len(divs_episodios))
        if len(divs_episodios) > 0:
            for div_ep in divs_episodios:
                atag_episodio = div_ep.find('a')
                href_episodio = atag_episodio['href']
                img_tag_episodio = atag_episodio.find('img')
                img_url_episodio = self.get_img_url(img_tag_episodio)
                array_episodio_temp = [text for text in atag_episodio.find('span', {
                    'class': 'info'}).stripped_strings]
                if len(array_episodio_temp) == 2:
                    type_episodio = array_episodio_temp[0]
                    title_episodio = array_episodio_temp[1]
                else:
                    type_episodio = array_episodio_temp[0]
                    title_episodio = ''
                third_page = self.get_page_bs4(href_episodio)
                if third_page:
                    div_links_epi = third_page.find_all('a', attrs={'class': 'cativ'})
                    if div_links_epi:
                        atag_ep_link = div_links_epi
                        if len(atag_ep_link) > 0:
                            ids = []
                            for a_url_epi in atag_ep_link:
                                if a_url_epi.has_attr('data-id'):
                                    data_id = str(a_url_epi['data-id'])
                                    data_episodio = str(a_url_epi['data-episodio'])
                                    data_player = str(a_url_epi['data-player'])
                                    url_data_id = 'https://canaismax.com/embed/' + data_id + '/' + data_episodio + '/' + data_player
                                    ids.append(url_data_id)
                            if len(ids) > 0:
                                self.save_episodio(ids, img_url_episodio, title_episodio, type_episodio, temporada)

    def save_episodio(self, ids, img_url_episodio, title_episodio, type_episodio, temporada):
        episodio = Episodio()
        episodio.temporada = temporada
        episodio.img_url = img_url_episodio
        episodio.type = type_episodio
        episodio.title = title_episodio
        episodio.save()
        for id_url_epi in ids:
            link = LinkSerie()
            link.url = id_url_epi
            link.episodio = episodio
            link.save()

    def get_img_url(self, img_tag):
        if img_tag.has_attr('src'):
            img_url = img_tag['src']
        elif img_tag.has_attr('data-src'):
            img_url = img_tag['data-src']
        else:
            img_url = ''
        return img_url

    def save_serie(self, ano, duracao, episodios, imdb, img_url, sinopse, temporadas, tipo, title):
        serie = Serie()
        serie.title = title
        serie.imdb = imdb
        serie.tipo = tipo
        serie.img_url = img_url
        serie.temporadas = temporadas
        serie.sinopse = sinopse
        serie.episodios = episodios
        serie.duracao = duracao
        serie.ano = ano
        serie.save()
        return serie

    def mine(self):
        try:
            Serie.objects.all().delete()
            Temporada.objects.all().delete()
            Episodio.objects.all().delete()
            LinkSerie.objects.all().delete()
            site = Site.objects.get(name='series')
            for category in site.categorychannel_set.all():
                self.extract(category)
            return True
        except (Exception,):
            return False

    def get_temporadas(self, param):
        if 'temporadas' in param:
            return param[:param.index(' temporadas')]
        else:
            return param[:param.index(' temporada')]
