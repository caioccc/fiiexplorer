import logging

import requests
from bs4 import BeautifulSoup
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView

from app.models import Channel, Link, Type

logging.basicConfig(level=logging.DEBUG)


def collect_canais(request):
    Channel.objects.all().delete()
    Link.objects.all().delete()
    Type.objects.all().delete()
    url_default = 'https://multicanais.com/aovivo/assistir-tv-online-gratis-hd-24h/page/'
    url_esportes = 'https://multicanais.com/aovivo/eventos-esportivos-online/page/'
    type1 = Type()
    type1.save()
    type2 = Type()
    type2.name = 'Esportes'
    type2.save()
    extract_channels_multicanais(url_default, 3, type1)
    extract_channels_multicanais(url_esportes, 2, type2)
    return redirect('/')


def collect_jogos(request):
    Channel.objects.filter(type__name__icontains='Esportes').delete()
    Link.objects.filter(channel__type__name__icontains='Esportes').delete()
    Type.objects.filter(name__icontains='Esportes').delete()
    url_esportes = 'https://multicanais.com/aovivo/eventos-esportivos-online/page/'
    type2 = Type()
    type2.name = 'Esportes'
    type2.save()
    extract_channels_multicanais(url_esportes, 2, type2)
    return redirect('/jogos')


def extract_channels_multicanais(url, pages, type):
    pages = pages + 1
    for i in range(1, pages):
        temp_url = url + str(i)
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
                                    ch.type = type
                                    ch.save()
                                    for id_url in ids:
                                        link = Link()
                                        link.url = id_url
                                        link.channel = ch
                                        link.save()


class CanaisView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    login_url = '/admin/login/'
    model = Channel
    context_object_name = 'canais'

    def get_queryset(self):
        if 'q' in self.request.GET:
            return Channel.objects.filter(title__icontains=self.request.GET['q'], type__name__icontains='Canais')
        return Channel.objects.filter(type__name__icontains='Canais')


class JogosView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    login_url = '/admin/login/'
    model = Channel
    context_object_name = 'canais'

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['jogos'] = True
        return super(JogosView, self).get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        if 'q' in self.request.GET:
            return Channel.objects.filter(title__icontains=self.request.GET['q'], type__name__icontains='Esportes')
        return Channel.objects.filter(type__name__icontains='Esportes')


class ViewChannel(LoginRequiredMixin, DetailView):
    template_name = 'view-channel.html'
    login_url = '/admin/login/'
    model = Channel
    pk_url_kwarg = 'pk'
    context_object_name = 'canal'


class ViewLink(LoginRequiredMixin, DetailView):
    template_name = 'view-link.html'
    login_url = '/admin/login/'
    model = Link
    context_object_name = 'link'
