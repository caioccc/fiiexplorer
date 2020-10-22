import json
import logging

import requests
from bs4 import BeautifulSoup
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
# Create your views here.
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView

from app.models import Channel, Link

logging.basicConfig(level=logging.DEBUG)


def collect_sites(request):
    Channel.objects.all().delete()
    Link.objects.all().delete()
    url_default = 'https://multicanais.com/aovivo/assistir-tv-online-gratis-hd-24h/page/'
    for i in range(1, 4):
        temp_url = url_default + str(i)
        req = requests.get(temp_url)
        if req.status_code == 200:
            page = BeautifulSoup(req.text, 'html.parser')
            divs_entries = page.find_all(attrs={"class": "entry-image"})
            if len(divs_entries) > 0:
                for div in divs_entries:
                    atag = div.find('a')
                    href = atag['href']
                    title = atag['title']
                    img_url = atag.find('img')['data-lazy-src']
                    other_req = requests.get(href)
                    if other_req.status_code == 200:
                        second_page = BeautifulSoup(other_req.text, 'html.parser')
                        div_links = second_page.find('div', attrs={'class': 'links'})
                        if div_links:
                            atags = div_links.find_all("a")
                            if len(atags) > 0:
                                ids = []
                                for a in atags:
                                    data_id = a['data-id']
                                    if 'http' in str(data_id):
                                        ids.append(str(data_id))
                                if len(ids) > 0:
                                    ch = Channel()
                                    ch.title = title
                                    ch.img_url = img_url
                                    ch.save()
                                    for id_url in ids:
                                        link = Link()
                                        link.url = id_url
                                        link.channel = ch
                                        link.save()
    return redirect('/')


class IndexView(ListView):
    template_name = 'index.html'
    model = Channel
    context_object_name = 'canais'

    def get_queryset(self):
        if 'q' in self.request.GET:
            return Channel.objects.filter(title__icontains=self.request.GET['q'])
        return Channel.objects.all()


class ViewChannel(DetailView):
    template_name = 'view-channel.html'
    model = Channel
    pk_url_kwarg = 'pk'
    context_object_name = 'canal'


class ViewLink(DetailView):
    template_name = 'view-link.html'
    model = Link
    context_object_name = 'link'
