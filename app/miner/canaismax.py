from app.miner.common import Miner
from app.models import Channel, Link, Site


class CustomMiner(Miner):

    def extract(self, category):
        pages = int(category.pages) + 1
        for i in range(1, pages):
            temp_url = self.get_page_url(category.url, 'canaismax', i)
            page = self.get_page_bs4(temp_url)
            if page:
                divs_entries = page.select('div.item>div.bloco-canal')
                print('total_canais', len(divs_entries))
                if len(divs_entries) > 0:
                    for div in divs_entries:
                        atag = div.find('a')
                        href = atag['href']
                        img_tag = atag.find('img')
                        if img_tag.has_attr('title'):
                            title = img_tag['title']
                        else:
                            title = ''
                        if img_tag.has_attr('src'):
                            img_url = img_tag['src']
                        elif img_tag.has_attr('data-src'):
                            img_url = img_tag['data-src']
                        else:
                            img_url = ''
                        second_page = self.get_page_bs4(href)
                        if second_page:
                            div_links = second_page.find_all('a', attrs={'class': 'cativ'})
                            channel_id = self.get_channel_id(str(second_page.select('script')[-1].contents[0]))
                            if div_links:
                                atags = div_links
                                if len(atags) > 0:
                                    ids = []
                                    for a in atags:
                                        if a.has_attr('data-link'):
                                            data_id = str(a['data-link'])
                                            if 'op=' in data_id:
                                                third_page_temp = self.get_page_bs4(data_id)
                                                if third_page_temp:
                                                    div_buttons = third_page_temp.find('div',
                                                                                       attrs={
                                                                                           'class': 'buttons-quality'})
                                                    if div_buttons:
                                                        novos_links = div_buttons.find_all('a')
                                                        if len(novos_links) > 0:
                                                            for alinks_temp in novos_links:
                                                                if alinks_temp.has_attr('href'):
                                                                    alink_temp_url = str(alinks_temp['href'])
                                                                    ids.append(alink_temp_url)
                                            else:
                                                print('normal', title)
                                                ids.append(data_id)
                                    if len(ids) > 0:
                                        ch = Channel()
                                        ch.title = (title[:230] + '..') if len(title) > 75 else title
                                        ch.img_url = img_url
                                        ch.category = category
                                        ch.channel_id = channel_id
                                        ch.save()
                                        for id_url in ids:
                                            link = Link()
                                            link.url = id_url
                                            link.channel = ch
                                            link.save()

    def mine(self):
        # try:
        Channel.objects.filter(category__site__name='canaismax').delete()
        Link.objects.filter(channel__category__site__name='canaismax').delete()
        site = Site.objects.get(name='canaismax')
        for category in site.categorychannel_set.all():
            self.extract(category)
        return True
        # except (Exception,):
        #     return False

    def get_channel_id(self, string_script):
        api_url = 'https://canaismax.com/api/canal/'
        if api_url in string_script:
            ind = string_script.index(api_url) + len(api_url)
            ind_bar = ind + 24
            id = string_script[ind:ind_bar]
            return id
        return ''
