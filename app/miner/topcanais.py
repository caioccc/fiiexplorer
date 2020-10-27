from app.miner.common import Miner
from app.models import Channel, Link, Site


class CustomMiner(Miner):

    def extract(self, category):
        pages = int(category.pages) + 1
        for i in range(1, pages):
            temp_url = self.get_page_url(category.url, 'topcanais', i)
            page = self.get_page_bs4(temp_url)
            if page:
                divs_entries = page.select('div[id=primary]>div>div.g1-collection-viewport>ul>li>article>figure')
                if len(divs_entries) > 0:
                    for div in divs_entries:
                        atag = div.find('a')
                        href = atag['href']
                        title = atag['title']
                        img_url = atag.find('div').find('img')['src']
                        second_page = self.get_page_bs4(href)
                        if second_page:
                            div_links = second_page.find('div', attrs={'class': 'canais'})
                            if div_links:
                                atags = div_links.find_all("a")
                                if len(atags) > 0:
                                    ids = []
                                    for a in atags:
                                        if a.has_attr('data-id'):
                                            data_id = str(a['data-id'])
                                            data_pasta = str(a['data-pasta'])
                                            data_playertipo = str(a['data-playertipo'])
                                            if data_playertipo == 'externo':
                                                print('externo', title)
                                                if a.has_attr('data-servidor'):
                                                    data_servidor = str(a['data-servidor'])
                                                else:
                                                    data_servidor = data_id
                                                url_id = 'https://topcanais.com/player/player.php?id=' + data_id + '&player=' + data_servidor
                                            elif data_playertipo == 'hls':
                                                print('hls', title)
                                                url_id = 'https://topcanais.com/player/hls.php?id=' + data_id
                                            else:
                                                print('normal', title)
                                                url_id = 'https://topcanais.com/player/aovivo.php?canal=' + data_id + '&pasta=' + data_pasta
                                            ids.append(url_id)
                                    if len(ids) > 0:
                                        ch = Channel()
                                        ch.title = title
                                        ch.img_url = img_url
                                        ch.category = category
                                        ch.save()
                                        for id_url in ids:
                                            link = Link()
                                            link.url = id_url
                                            link.channel = ch
                                            link.save()

    def mine(self):
        try:
            Channel.objects.filter(category__site__name='topcanais').delete()
            Link.objects.filter(channel__category__site__name='topcanais').delete()
            site = Site.objects.get(name='topcanais')
            for category in site.categorychannel_set.all():
                self.extract(category)
            return True
        except (Exception,):
            return False
