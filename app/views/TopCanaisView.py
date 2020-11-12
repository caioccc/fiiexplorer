import re
from threading import Thread

import requests
from bs4 import BeautifulSoup
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView

from app.miner.explorer import mineAllTopCanais, mineChannelTopCanais
from app.models import Site, Channel
from app.utils import request_json, remove_iv, get_text_type, clean_title


class CollectAllTopCanais(TemplateView):
    template_name = 'topcanais.html'

    def get(self, request, *args, **kwargs):
        site = Site.objects.get(name='topcanais')
        site.done = False
        site.save()
        Thread(target=mineAllTopCanais).start()
        return redirect('/topcanais')


class TopCanaisView(LoginRequiredMixin, ListView):
    template_name = 'topcanais.html'
    login_url = '/admin/login/'
    model = Channel
    context_object_name = 'canais'

    def get_context_data(self, *, object_list=None, **kwargs):
        json = request_json()
        kwargs['json'] = [json[i:i + 4] for i in range(0, len(json), 4)]
        kwargs['num_pages'] = len(json) / 4
        kwargs['total_items'] = len(json)
        return super(TopCanaisView, self).get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        if 'q' in self.request.GET:
            return Channel.objects.filter(title__icontains=self.request.GET['q'], category__site__name='topcanais')
        return Channel.objects.filter(category__site__name='topcanais')


class ViewChannelTopCanais(LoginRequiredMixin, DetailView):
    template_name = 'view-channel-topcanais.html'
    login_url = '/admin/login/'
    model = Channel
    pk_url_kwarg = 'pk'
    context_object_name = 'canal'

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['SITE_URL'] = 'http://'+self.request.META['HTTP_HOST'] + '/'
        return super(ViewChannelTopCanais, self).get_context_data(object_list=object_list, **kwargs)


class CollectChannelTopCanais(DetailView):
    template_name = 'index.html'
    model = Channel

    def get(self, request, *args, **kwargs):
        canal = self.get_object()
        canal.link_set.all().delete()
        Thread(target=mineChannelTopCanais, kwargs=dict(pk=canal.pk)).start()
        return redirect('/topcanais/' + str(canal.pk))


def playlist_m3u8_topcanais(request):
    headers = {'origin': 'https://topcanais.com', 'referer': 'https://topcanais.com/'}
    uri_m3u8 = request.GET['uri']
    try:
        req = requests.get(url=uri_m3u8, headers=headers)
        page = BeautifulSoup(req.text, 'html.parser')
        page_str = str(page.contents[0])
        arr_strings_without_http = list(set(remove_iv(re.findall("([^\s]+.m3u8)", page_str))))
        if len(arr_strings_without_http) > 0:
            playlist_index = str(uri_m3u8).index('playlist.m3u8')
            prefix = str(uri_m3u8)[:playlist_index]
            for i in range(len(arr_strings_without_http)):
                new_uri = prefix + str(arr_strings_without_http[i])
                page_str = page_str.replace(arr_strings_without_http[i],
                                            'http://'+request.META['HTTP_HOST'] + '/' + 'api/topcanais/other/playlist.m3u8?uri=' + str(new_uri))
        else:
            arr_strings = list(set(remove_iv(re.findall("(?P<url>https?://[^\s]+)", page_str))))
            page_str = replace_page_str(arr_strings, page_str, request)
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


def playlist_other_m3u8_topcanais(request):
    headers = {'origin': 'https://topcanais.com', 'referer': 'https://topcanais.com/'}
    uri_m3u8 = request.GET['uri']
    try:
        req = requests.get(url=uri_m3u8, headers=headers)
        page = BeautifulSoup(req.text, 'html.parser')
        page_str = str(page.contents[0])
        arr_strings = list(set(remove_iv(re.findall("(?P<url>https?://[^\s]+)", page_str))))
        page_str = replace_page_str(arr_strings, page_str, request)
        return HttpResponse(
            content=page_str,
            status=req.status_code,
            content_type=req.headers['Content-Type']
        )
    except (Exception,):
        return HttpResponseNotFound("hello")


def replace_page_str(arr_strings, page_str, request):
    if len(arr_strings) > 0:
        for i in range(len(arr_strings)):
            if not 'key?id=' in str(arr_strings[i]):
                page_str = page_str.replace(arr_strings[i],
                                            'http://'+request.META['HTTP_HOST'] + '/'  + 'api/topcanais/ts?link=' + str(arr_strings[i]))
        for uri_ts_coded in arr_strings:
            if 'key?id=' in str(uri_ts_coded):
                page_str = page_str.replace(uri_ts_coded,
                                            'http://'+request.META['HTTP_HOST'] + '/'  + 'api/topcanais/ts?link=' + str(uri_ts_coded))
                break
    return page_str


def get_ts_topcanais(request):
    key = request.GET['link']
    headers = {'origin': 'https://topcanais.com', 'referer': 'https://topcanais.com/'}
    try:
        req = requests.get(url=key, stream=True, timeout=60, headers=headers)
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


def get_lista_topcanais(request):
    f = open("lista-topcanais.m3u8", "a")
    f.truncate(0)
    f.write("#EXTM3U\n")
    for ch in Channel.objects.filter(category__site__name='topcanais', link__m3u8__icontains='.m3u8').distinct():
        for link in ch.link_set.filter(m3u8__icontains='.m3u8').distinct():
            str_type = get_text_type(link)
            if str_type:
                title = str_type + ' ' + clean_title(ch)
                custom_m3u8 = 'http://'+request.META['HTTP_HOST'] + '/'  + 'api/topcanais/other/playlist.m3u8?uri=' + link.m3u8
            else:
                title = clean_title(ch)
                custom_m3u8 = 'http://'+request.META['HTTP_HOST'] + '/'  + 'api/topcanais/playlist.m3u8?uri=' + link.m3u8
            f.write('#EXTINF:{}, tvg-id="{} - {}" tvg-name="{} - {}" tvg-logo="{}" group-title="{}",{}\n{}\n'.format(
                link.id,
                link.id,
                title,
                title,
                link.id,
                ch.img_url,
                '',
                title,
                custom_m3u8))
    fsock = open("lista-topcanais.m3u8", "rb")
    return HttpResponse(fsock, content_type='text')
