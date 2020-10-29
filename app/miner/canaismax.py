from app.miner.common import Miner
from app.utils import get_page_bs4, save_link_channel, get_channel_id, get_img_url, make_ids
from app.models import Channel, Link, Site


class CustomMiner(Miner):

    def extract(self, category):
        pages = int(category.pages) + 1
        for i in range(1, pages):
            temp_url = self.get_page_url(category.url, 'canaismax', i)
            page = get_page_bs4(temp_url)
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
                        img_url = get_img_url(img_tag)
                        second_page = get_page_bs4(href)
                        if second_page:
                            div_links = second_page.find_all('a', attrs={'class': 'cativ'})
                            channel_id = get_channel_id(str(second_page.select('script')[-1].contents[0]))
                            if div_links:
                                atags = div_links
                                if len(atags) > 0:
                                    ids = make_ids(atags)
                                    if len(ids) > 0:
                                        ch = Channel()
                                        ch.title = (title[:230] + '..') if len(title) > 75 else title
                                        ch.img_url = img_url
                                        ch.category = category
                                        ch.channel_id = channel_id
                                        ch.url_site = str(href)
                                        ch.save()
                                        for id_url in ids:
                                            save_link_channel(ch, id_url)

    def mine(self):
        try:
            Channel.objects.filter(category__site__name='canaismax').delete()
            Link.objects.filter(channel__category__site__name='canaismax').delete()
            site = Site.objects.get(name='canaismax')
            for category in site.categorychannel_set.all():
                self.extract(category)
            return True
        except (Exception,):
            return False


