import re
import time
from threading import Thread

import requests
from bs4 import BeautifulSoup
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.views.generic import DetailView, TemplateView, ListView

from app.miner.explorer import mineAllAoVivoGratis, mineChannelAoVivoGratis, snifferAoVivoGratis
from app.models import Channel, Site
from app.utils import remove_iv, get_m3u8_aovivogratis_by_eval, \
    clean_title


class SnifferAoVivoGratis(TemplateView):
    template_name = 'aovivogratis.html'

    def get(self, request, *args, **kwargs):
        Thread(target=snifferAoVivoGratis).start()
        return redirect('/aovivogratis')


class CollectAllAoVivoGratis(TemplateView):
    template_name = 'aovivogratis.html'

    def get(self, request, *args, **kwargs):
        site = Site.objects.get(name='aovivogratis')
        site.done = False
        site.save()
        Thread(target=mineAllAoVivoGratis).start()
        return redirect('/aovivogratis')


class AoVivoGratisView(LoginRequiredMixin, ListView):
    template_name = 'aovivogratis.html'
    login_url = '/admin/login/'
    model = Channel
    context_object_name = 'canais'

    def get_context_data(self, *, object_list=None, **kwargs):
        return super(AoVivoGratisView, self).get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        if 'q' in self.request.GET:
            return Channel.objects.filter(title__icontains=self.request.GET['q'], category__site__name='aovivogratis')
        return Channel.objects.filter(category__site__name='aovivogratis')


class ViewChannelAoVivoGratis(LoginRequiredMixin, DetailView):
    template_name = 'view-channel-aovivogratis.html'
    login_url = '/admin/login/'
    model = Channel
    pk_url_kwarg = 'pk'
    context_object_name = 'canal'

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['SITE_URL'] = 'http://' + self.request.META['HTTP_HOST'] + '/'
        channel = self.get_object()
        string_m3u8 = get_m3u8_aovivogratis_by_eval(channel.url_site)
        kwargs['source'] = string_m3u8
        return super(ViewChannelAoVivoGratis, self).get_context_data(object_list=object_list, **kwargs)


def playlist_m3u8_aovivogratis(request):
    uri_m3u8 = request.GET['uri']
    headers = {'origin': 'https://player.aovivotv.xyz', 'referer': 'https://player.aovivotv.xyz/'}
    try:
        req = requests.get(url=uri_m3u8, headers=headers)
        page = BeautifulSoup(req.text, 'html.parser')
        page_str = str(page.contents[0])
        arr_strings = list(set(remove_iv(re.findall("([^\s]+.ts)", page_str))))
        if len(arr_strings) > 0:
            index_ = str(uri_m3u8).index('playlist.m3u8')
            prefix = uri_m3u8[:index_]
            for i in range(len(arr_strings)):
                new_uri = prefix + arr_strings[i]
                page_str = page_str.replace(arr_strings[i],
                                            'http://' + request.META['HTTP_HOST'] + '/api/aovivogratis/ts?link=' + str(
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


def get_ts_aovivogratis(request):
    key = request.GET['link']
    headers = {'origin': 'https://player.aovivotv.xyz', 'referer': 'https://player.aovivotv.xyz/'}
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


def gen_lista_aovivogratis(request):
    f = open("lista-aovivo.m3u8", "a")
    f.truncate(0)
    f.write("#EXTM3U\n")
    for ch in Channel.objects.filter(category__site__name='aovivogratis', link__m3u8__icontains='.m3u8').distinct():
        title = clean_title(ch)
        custom_m3u8 = ch.link_set.first().m3u8
        f.write('#EXTINF:{}, tvg-id="{} - {}" tvg-name="{} - {}" tvg-logo="{}" group-title="{}",{}\n{}\n'.format(
            ch.id,
            ch.id,
            title,
            title,
            ch.id,
            ch.img_url,
            '',
            title,
            custom_m3u8))
    f.close()
    fsock = open("lista-aovivo.m3u8", "rb")
    return HttpResponse(fsock, content_type='text')
