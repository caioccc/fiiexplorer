import re
from threading import Thread

import requests
from bs4 import BeautifulSoup
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.views.generic import DetailView, TemplateView, ListView

from app.miner.explorer import mineSeriePk, mineSeries
from app.models import Serie, Temporada, Site
from app.utils import remove_iv, clean_title


class CollectSerie(DetailView):
    template_name = 'series.html'
    model = Serie

    def get(self, request, *args, **kwargs):
        serie = self.get_object()
        for temp in Temporada.objects.filter(serie=serie):
            temp.episodio_set.all().delete()
        serie.temporada_set.all().delete()
        Thread(target=mineSeriePk, kwargs=dict(pk=serie.pk)).start()
        return redirect('/series/' + str(serie.pk))


class CollectSeries(TemplateView):
    template_name = 'series.html'

    def get(self, request, *args, **kwargs):
        site = Site.objects.get(name='series')
        site.done = False
        site.save()
        Thread(target=mineSeries).start()
        return redirect('/series')


class SeriesView(LoginRequiredMixin, ListView):
    template_name = 'series.html'
    login_url = '/admin/login/'
    model = Serie
    context_object_name = 'series'

    def get_queryset(self):
        if 'q' in self.request.GET:
            return Serie.objects.filter(title__icontains=self.request.GET['q'])
        return Serie.objects.all()


class ViewSerie(LoginRequiredMixin, DetailView):
    template_name = 'view-serie.html'
    login_url = '/admin/login/'
    model = Serie
    pk_url_kwarg = 'pk'
    context_object_name = 'serie'


def playlist_m3u8_series_canaismax(request):
    uri_m3u8 = request.GET['uri']
    headers = {'origin': 'https://canaismax.com', 'referer': 'https://canaismax.com'}
    try:
        req = requests.get(url=uri_m3u8, headers=headers)
        page = BeautifulSoup(req.text, 'html.parser')
        page_str = str(page.contents[0])
        arr_strings = list(set(remove_iv(re.findall("([^\s]+.ts)", page_str))))
        if len(arr_strings) > 0:
            for i in range(len(arr_strings)):
                page_str = page_str.replace(arr_strings[i],
                                            'http://' + request.META[
                                                'HTTP_HOST'] + '/' + 'api/series/canaismax/ts?link=' + str(
                                                arr_strings[i]))

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


def get_ts_series_canaismax(request):
    key = request.GET['link']
    headers = {'origin': 'https://canaismax.com', 'referer': 'https://canaismax.com'}
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


def gen_lista_series_canaismax(request):
    f = open("series-canaismax.m3u8", "a")
    f.truncate(0)
    f.write("#EXTM3U\n")
    for serie in Serie.objects.all():
        for temp in serie.temporada_set.all():
            for epi in temp.episodio_set.all():
                link = epi.linkserie_set.all().first()
                title = str(clean_title(serie)) + ' ' + str(epi.type) + ' - ' + str(epi.title)
                custom_m3u8 = 'http://' + request.META['HTTP_HOST'] + '/' + 'api/series/canaismax/playlist.m3u8?uri=' + str(link.m3u8)
                f.write(
                    '#EXTINF:{}, tvg-id="{} - {}" tvg-name="{} - {}" tvg-logo="{}" group-title="{}",{}\n{}\n'.format(
                        link.id,
                        link.id,
                        title,
                        title,
                        link.id,
                        serie.img_url,
                        '',
                        title,
                        custom_m3u8))
    fsock = open("series-canaismax.m3u8", "rb")
    return HttpResponse(fsock, content_type='text')
