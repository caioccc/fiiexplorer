import re
from threading import Thread

import requests
from bs4 import BeautifulSoup
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView

from app.miner.explorer import mineFilmes, mineFilmeOneCanaisMax
from app.models import Site, Filme
from app.utils import remove_iv, clean_title


class CollectFilmesCanaisMax(TemplateView):
    template_name = 'filmes.html'

    def get(self, request, *args, **kwargs):
        site = Site.objects.get(name='filmes')
        site.done = False
        site.save()
        Thread(target=mineFilmes).start()
        return redirect('/filmes')


class CollectFilmeOneCanaisMax(DetailView):
    template_name = 'index.html'
    model = Filme

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.url_set.all().delete()
        Thread(target=mineFilmeOneCanaisMax, kwargs=dict(pk=filme.pk)).start()
        return redirect('/view-film/' + str(filme.pk))


class FilmesView(LoginRequiredMixin, ListView):
    template_name = 'filmes.html'
    login_url = '/admin/login/'
    model = Filme
    context_object_name = 'filmes'

    def get_context_data(self, *, object_list=None, **kwargs):
        return super(FilmesView, self).get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        if 'q' in self.request.GET:
            return Filme.objects.filter(title__icontains=self.request.GET['q'])
        return Filme.objects.all()


class ViewFilmCanaisMax(LoginRequiredMixin, DetailView):
    template_name = 'view-filme.html'
    login_url = '/admin/login/'
    model = Filme
    pk_url_kwarg = 'pk'
    context_object_name = 'filme'

    def get_context_data(self, *, object_list=None, **kwargs):
        return super(ViewFilmCanaisMax, self).get_context_data(object_list=object_list, **kwargs)


def playlist_m3u8_filmes_canaismax(request):
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
                                            'http://'+request.META['HTTP_HOST'] + '/' + 'api/filmes/canaismax/ts?link=' + str(arr_strings[i]))

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


def get_ts_filmes_canaismax(request):
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


def gen_lista_filmes_canaismax(request):
    f = open("filmes-canaismax.m3u8", "a")
    f.truncate(0)
    f.write("#EXTM3U\n")
    for ch in Filme.objects.all():
        for link in ch.url_set.filter(m3u8__icontains='.m3u8').distinct():
            title = clean_title(ch)
            custom_m3u8 = 'http://'+request.META['HTTP_HOST'] + '/' + 'api/filmes/canaismax/playlist.m3u8?uri=' + link.m3u8
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
    fsock = open("filmes-canaismax.m3u8", "rb")
    return HttpResponse(fsock, content_type='text')
