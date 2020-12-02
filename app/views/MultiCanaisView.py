import re
from threading import Thread

import requests
from bs4 import BeautifulSoup
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect
from django.views.generic import DetailView, TemplateView, ListView

from app.miner.explorer import mineChannelMultiCanais, mineAllMultiCanais
from app.models import Channel, Site
from app.utils import clean_title, remove_iv, check_m3u8_req


class CollectChannelMultiCanais(DetailView):
    template_name = 'index.html'
    model = Channel

    def get(self, request, *args, **kwargs):
        canal = self.get_object()
        canal.link_set.all().delete()
        Thread(target=mineChannelMultiCanais, kwargs=dict(pk=canal.pk)).start()
        return redirect('/multicanais/' + str(canal.pk))


class CollectAllMultiCanais(TemplateView):
    template_name = 'multicanais.html'

    def get(self, request, *args, **kwargs):
        site = Site.objects.get(name='multicanais')
        site.done = False
        site.save()
        Thread(target=mineAllMultiCanais).start()
        return redirect('/')


class MultiCanaisView(LoginRequiredMixin, ListView):
    template_name = 'multicanais.html'
    login_url = '/admin/login/'
    model = Channel
    context_object_name = 'canais'

    def get_context_data(self, *, object_list=None, **kwargs):
        return super(MultiCanaisView, self).get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        if 'q' in self.request.GET:
            return Channel.objects.filter(Q(title__icontains=self.request.GET['q']),
                                          Q(link__m3u8__icontains='.m3u8'),
                                          Q(category__site__name='multicanais')).distinct()
        return Channel.objects.filter(Q(link__m3u8__icontains='.m3u8'), Q(category__site__name='multicanais')).distinct()


class ViewChannelMultiCanais(LoginRequiredMixin, DetailView):
    template_name = 'view-channel-multicanais.html'
    login_url = '/admin/login/'
    model = Channel
    pk_url_kwarg = 'pk'
    context_object_name = 'canal'

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['SITE_URL'] = 'http://' + self.request.META['HTTP_HOST'] + '/'
        return super(ViewChannelMultiCanais, self).get_context_data(object_list=object_list, **kwargs)


def playlist_m3u8_multicanais(request):
    uri_m3u8 = request.GET['uri']
    headers = {'origin': 'https://esporteone.com', 'referer': 'https://esporteone.com'}
    try:
        req = requests.get(url=uri_m3u8, headers=headers)
        page = BeautifulSoup(req.text, 'html.parser')
        page_str = str(page.contents[0])
        arr_strings = list(set(remove_iv(re.findall("([^\s]+.ts)", page_str))))
        if len(arr_strings) > 0:
            index_ = str(uri_m3u8).index('video.m3u8')
            prefix = uri_m3u8[:index_]
            for i in range(len(arr_strings)):
                new_uri = prefix + arr_strings[i]
                page_str = page_str.replace(arr_strings[i],
                                            'http://' + request.META['HTTP_HOST'] + '/api/multi/ts?link=' + str(
                                                new_uri))

        return HttpResponse(
            content=page_str,
            status=req.status_code,
            content_type=req.headers['Content-Type']
        )
    except (requests.exceptions.ConnectionError,):
        print('erro ao connectar')
        return HttpResponseNotFound()
    except (Exception,):
        return HttpResponseNotFound("hello")


def get_ts_multicanais(request):
    key = request.GET['link']
    headers = {'origin': 'https://esporteone.com', 'referer': 'https://esporteone.com'}
    try:
        req = requests.get(url=key, stream=True, timeout=120, headers=headers)
        if req.status_code == 200:
            return HttpResponse(
                content=req.content,
                status=req.status_code,
                content_type=req.headers['Content-Type']
            )
        else:
            return HttpResponseNotFound("hello")
    except (Exception,):
        return HttpResponseNotFound("hello")


def check_channel_title_especific(title_channel):
    title_channel = str(title_channel)
    canais = ['DAZN', 'ESPN', 'Rede TV', 'Premiere', 'Cult', 'Disney']
    for title in canais:
        if title in title_channel:
            return True
    return False


def gen_lista_multicanais(request):
    f = open("lista-multicanais.m3u8", "a")
    f.truncate(0)
    f.write("#EXTM3U\n")
    for ch in Channel.objects.filter(category__site__name='multicanais', link__m3u8__icontains='.m3u8').distinct():
        link = ch.link_set.all().first()
        title = clean_title(ch)
        custom_m3u8 = 'http://' + request.META['HTTP_HOST'] + '/api/multi/playlist.m3u8?uri=' + link.m3u8
        f.write('#EXTINF:{}, tvg-id="{} - {}" tvg-name="{} - {}" tvg-logo="{}" group-title="{}",{}\n{}\n'.format(
            link.id,
            link.id,
            title,
            title,
            link.id,
            ch.img_url,
            'Canais Ao Vivo',
            title,
            custom_m3u8))
    f.close()
    fsock = open("lista-multicanais.m3u8", "rb")
    return HttpResponse(fsock, content_type='text')


def api_multicanais(request):
    headers = {'origin': 'https://esporteone.com', 'referer': 'https://esporteone.com'}
    lista_geral = Channel.objects.filter(category__site__name='multicanais', link__m3u8__icontains='.m3u8').distinct()
    entries = []
    for ch in lista_geral:
        link = ch.link_set.all().first()
        title = clean_title(ch)
        custom_m3u8 = 'http://' + request.META['HTTP_HOST'] + '/api/multi/playlist.m3u8?uri=' + link.m3u8
        if check_channel_title_especific(ch.title):
            for link in ch.link_set.all():
                if check_m3u8_req(link.m3u8, headers=headers):
                    title = clean_title(ch)
                    custom_m3u8 = 'http://' + request.META['HTTP_HOST'] + '/api/multi/playlist.m3u8?uri=' + link.m3u8
        entries.append({'id': str(ch.id),
                        'name': str(title),
                        'm3u8': str(custom_m3u8),
                        'uri': str(custom_m3u8),
                        'img_url': str(ch.img_url)})
    return JsonResponse(entries, safe=False)
