from app.miner.common import Miner
from app.utils import get_page_bs4, get_img_url, save_temporada, get_url_temporada, get_episodios
from app.models import Site, Serie, Episodio, LinkSerie, Temporada


class CustomMiner(Miner):

    def extract(self, category):
        pages = int(category.pages) + 1
        for i in range(1, pages):
            temp_url = self.get_page_url(category.url, 'series', i)
            page = get_page_bs4(temp_url)
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
                        img_url = get_img_url(img_tag)
                        second_page = get_page_bs4(href)
                        if second_page:
                            sinopse = '' if len(second_page.select('section.description')) == 0 else \
                                second_page.select('section.description')[0].get_text()
                            array_temp_details = [text for text in second_page.find('section', {
                                'class': 'details-filme'}).stripped_strings]
                            episodios = str(array_temp_details[0])
                            duracao = str(array_temp_details[1])
                            ano = str(array_temp_details[2])
                            serie = self.save_serie(ano, duracao, episodios, imdb, img_url, sinopse, temporadas, tipo,
                                                    title, href)
                            temporada_obj = save_temporada(serie, 1)
                            get_episodios(second_page, temporada_obj)
                            if int(temporadas) > 1:
                                for i_temp in range(2, (int(temporadas) + 1)):
                                    second_page_temps = get_page_bs4(get_url_temporada(href, i_temp))
                                    if second_page_temps:
                                        temporada_obj_temp = save_temporada(serie, int(i_temp))
                                        get_episodios(second_page_temps, temporada_obj_temp)

    def save_serie(self, ano, duracao, episodios, imdb, img_url, sinopse, temporadas, tipo, title, href):
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
        serie.url_site = str(href)
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
