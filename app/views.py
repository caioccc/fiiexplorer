import datetime
import logging
import re
from threading import Thread

# Create your views here.
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, TemplateView

from app.miner.explorer import mineTopCanais, mineCanaisMax, mineFilmes, mineSeries, mineSeriePk, mineCanalPk, \
    mineMultiCanais, mineCanalMultiCanais
from app.models import Channel, Site, Filme, Serie, Temporada
from app.utils import get_headers
from fiiexplorer.settings import SITE_URL

logging.basicConfig(level=logging.DEBUG)


class CollectCanal(DetailView):
    template_name = 'index.html'
    model = Channel

    def get(self, request, *args, **kwargs):
        canal = self.get_object()
        canal.link_set.all().delete()
        Thread(target=mineCanalPk, kwargs=dict(pk=canal.pk)).start()
        return redirect('/view-channel/' + str(canal.pk))


class CollectCanalMultiCanais(DetailView):
    template_name = 'index.html'
    model = Channel

    def get(self, request, *args, **kwargs):
        canal = self.get_object()
        canal.link_set.all().delete()
        Thread(target=mineCanalMultiCanais, kwargs=dict(pk=canal.pk)).start()
        return redirect('/view-channel/' + str(canal.pk))


class CollectSerie(DetailView):
    template_name = 'series.html'
    model = Serie

    def get(self, request, *args, **kwargs):
        serie = self.get_object()
        for temp in Temporada.objects.filter(serie=serie):
            temp.episodio_set.all().delete()
        serie.temporada_set.all().delete()
        Thread(target=mineSeriePk, kwargs=dict(pk=serie.pk)).start()
        return redirect('/view-serie/' + str(serie.pk))


class CollectSeries(TemplateView):
    template_name = 'series.html'

    def get(self, request, *args, **kwargs):
        site = Site.objects.get(name='series')
        site.done = False
        site.save()
        Thread(target=mineSeries).start()
        return redirect('/series')


class CollectFilmes(TemplateView):
    template_name = 'filmes.html'

    def get(self, request, *args, **kwargs):
        site = Site.objects.get(name='filmes')
        site.done = False
        site.save()
        Thread(target=mineFilmes).start()
        return redirect('/filmes')


class CollectMultiCanais(TemplateView):
    template_name = 'multicanais.html'

    def get(self, request, *args, **kwargs):
        site = Site.objects.get(name='multicanais')
        site.done = False
        site.save()
        Thread(target=mineMultiCanais).start()
        return redirect('/multicanais')


class CollectTopCanais(TemplateView):
    template_name = 'topcanais.html'

    def get(self, request, *args, **kwargs):
        site = Site.objects.get(name='topcanais')
        site.done = False
        site.save()
        Thread(target=mineTopCanais).start()
        return redirect('/')


class CollectCanaisMax(TemplateView):
    template_name = 'canaismax.html'

    def get(self, request, *args, **kwargs):
        site = Site.objects.get(name='canaismax')
        site.done = False
        site.save()
        Thread(target=mineCanaisMax).start()
        return redirect('/canaismax')


class SeriesView(LoginRequiredMixin, ListView):
    template_name = 'series.html'
    login_url = '/admin/login/'
    model = Serie
    context_object_name = 'series'

    def get_queryset(self):
        if 'q' in self.request.GET:
            return Serie.objects.filter(title__icontains=self.request.GET['q'])
        return Serie.objects.all()


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


class MultiCanaisView(LoginRequiredMixin, ListView):
    template_name = 'multicanais.html'
    login_url = '/admin/login/'
    model = Channel
    context_object_name = 'canais'

    def get_context_data(self, *, object_list=None, **kwargs):
        json = request_json()
        kwargs['json'] = [json[i:i + 4] for i in range(0, len(json), 4)]
        kwargs['num_pages'] = len(json) / 4
        kwargs['total_items'] = len(json)
        return super(MultiCanaisView, self).get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        if 'q' in self.request.GET:
            return Channel.objects.filter(title__icontains=self.request.GET['q'], category__site__name='multicanais')
        return Channel.objects.filter(category__site__name='multicanais')


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


class ViewFilm(LoginRequiredMixin, DetailView):
    template_name = 'view-filme.html'
    login_url = '/admin/login/'
    model = Filme
    pk_url_kwarg = 'pk'
    context_object_name = 'filme'

    def get_context_data(self, *, object_list=None, **kwargs):
        return super(ViewFilm, self).get_context_data(object_list=object_list, **kwargs)


class ViewChannel(LoginRequiredMixin, DetailView):
    template_name = 'view-channel.html'
    login_url = '/admin/login/'
    model = Channel
    pk_url_kwarg = 'pk'
    context_object_name = 'canal'

    def get(self, request, *args, **kwargs):
        return super(ViewChannel, self).get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs = self.insert_context_data(**kwargs)
        kwargs['SITE_URL'] = SITE_URL
        return super(ViewChannel, self).get_context_data(object_list=object_list, **kwargs)

    def insert_context_data(self, **kwargs):
        if self.get_object().channel_id:
            channel_id = self.get_object().channel_id
            today_date = get_date_now()
            url = 'https://canaismax.com/api/canal/' + channel_id + '/' + str(today_date)
            req = requests.get(url)
            now = round(datetime.datetime.now().timestamp())
            if req.status_code == 200:
                dic_complete = req.json()
                p_atual = None
                for program in dic_complete:
                    if (int(program['inicio']) <= now) and (int(program['fim']) > now):
                        p_atual = program
                p_next = None
                for program in dic_complete:
                    if p_atual['fim'] == program['inicio']:
                        p_next = program
                kwargs['program_1'] = p_atual
                kwargs['program_2'] = p_next
        return kwargs


class ViewSerie(LoginRequiredMixin, DetailView):
    template_name = 'view-serie.html'
    login_url = '/admin/login/'
    model = Serie
    pk_url_kwarg = 'pk'
    context_object_name = 'serie'


class CanaisMaxView(LoginRequiredMixin, ListView):
    template_name = 'canaismax.html'
    login_url = '/admin/login/'
    model = Channel
    context_object_name = 'canais'

    def get(self, request, *args, **kwargs):
        return super(CanaisMaxView, self).get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        json = request_json()
        kwargs['json'] = [json[i:i + 4] for i in range(0, len(json), 4)]
        kwargs['num_pages'] = len(json) / 4
        kwargs['total_items'] = len(json)
        return super(CanaisMaxView, self).get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        if 'q' in self.request.GET:
            return Channel.objects.filter(title__icontains=self.request.GET['q'],
                                          category__site__name='canaismax',
                                          link__m3u8__icontains='.m3u8').distinct()
        return Channel.objects.filter(category__site__name='canaismax', link__m3u8__icontains='.m3u8').distinct()


def get_date_now():
    now = datetime.datetime.now()
    month = str("0") + str(now.month) if now.month < 10 else now.month
    day = str("0") + str(now.day) if now.day < 10 else now.day
    return '%s-%s-%s' % (now.year, month, day)


def request_json():
    api_url = 'https://canaismax.com/api/programacao'
    req = requests.get(api_url)
    if req.status_code == 200:
        json = req.json()
        return json
    return None


def get_json(request):
    json = request_json()
    return JsonResponse(json, safe=False)


def check_m3u8_req(uri):
    try:
        headers = get_headers()
        req = requests.get(uri, headers=headers)
        if req.status_code == 200:
            size = 0
            for chunk in req.iter_content(256):
                size += len(chunk)
                if size > 4096:
                    return True
        return False
    except (Exception,):
        print('Break ao checar m3u8')
        return False


def generate_m3u_multicanais(request):
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
                                            SITE_URL + 'multi/ts?link=' + str(new_uri))

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


def generate_m3u(request):
    headers = {'origin': 'https://canaismax.com', 'referer': 'https://canaismax.com/'}
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
                                            SITE_URL + 'api/other/playlist.m3u8?uri=' + str(new_uri))
        else:
            arr_strings = list(set(remove_iv(re.findall("(?P<url>https?://[^\s]+)", page_str))))
            if len(arr_strings) > 0:
                for i in range(len(arr_strings)):
                    if not 'key?id=' in str(arr_strings[i]):
                        page_str = page_str.replace(arr_strings[i],
                                                    SITE_URL + 'ts?link=' + str(arr_strings[i]))
                for uri_ts_coded in arr_strings:
                    if 'key?id=' in str(uri_ts_coded):
                        page_str = page_str.replace(uri_ts_coded,
                                                    SITE_URL + 'ts?link=' + str(uri_ts_coded))
                        break

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


def get_other_m3u(request):
    headers = {'origin': 'https://canaismax.com', 'referer': 'https://canaismax.com/'}
    uri_m3u8 = request.GET['uri']
    try:
        req = requests.get(url=uri_m3u8, headers=headers)
        page = BeautifulSoup(req.text, 'html.parser')
        page_str = str(page.contents[0])
        arr_strings = list(set(remove_iv(re.findall("(?P<url>https?://[^\s]+)", page_str))))
        if len(arr_strings) > 0:
            for i in range(len(arr_strings)):
                if not 'key?id=' in str(arr_strings[i]):
                    page_str = page_str.replace(arr_strings[i],
                                                SITE_URL + 'ts?link=' + str(arr_strings[i]))
            for uri_ts_coded in arr_strings:
                if 'key?id=' in str(uri_ts_coded):
                    page_str = page_str.replace(uri_ts_coded,
                                                SITE_URL + 'ts?link=' + str(uri_ts_coded))
                    break
        return HttpResponse(
            content=page_str,
            status=req.status_code,
            content_type=req.headers['Content-Type']
        )
    except (Exception,):
        return HttpResponseNotFound("hello")


def get_ts(request):
    key = request.GET['link']
    headers = get_headers()
    print(key)
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


def remove_iv(array_uri):
    for i in range(len(array_uri)):
        if '",IV' in str(array_uri[i]):
            index_iv = str(array_uri[i]).index('",IV=')
            if index_iv >= 0:
                array_uri[i] = str(array_uri[i])[:index_iv]
    return array_uri


def get_text_type(link):
    uri = str(link.m3u8)
    if 'sd/' in uri:
        return 'SD'
    elif 'hd/' in uri:
        return 'HD'
    else:
        return None


def clean_title(channel):
    title = str(channel.title)
    if 'Assistir ' in title:
        if ' ao vivo' in title:
            return title[(title.index('Assistir ') + len('Assistir ')):title.index(' ao vivo')]
    return title


def get_lista_multicanais(request):
    f = open("playlist.m3u8", "a")
    f.truncate(0)
    f.write("#EXTM3U\n")
    for ch in Channel.objects.filter(category__site__name='multicanais', link__m3u8__icontains='.m3u8').distinct():
        for link in ch.link_set.filter(m3u8__icontains='.m3u8').distinct():
            title = clean_title(ch)
            custom_m3u8 = SITE_URL + 'api/multi/playlist.m3u8?uri=' + link.m3u8
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
    fsock = open("playlist.m3u8", "rb")
    return HttpResponse(fsock, content_type='text')


def get_lista_gen(request):
    f = open("lista.m3u8", "a")
    f.truncate(0)
    f.write("#EXTM3U\n")
    for ch in Channel.objects.filter(category__site__name='canaismax', link__m3u8__icontains='.m3u8').distinct():
        for link in ch.link_set.filter(m3u8__icontains='.m3u8').distinct():
            str_type = get_text_type(link)
            if str_type:
                title = str_type + ' ' + clean_title(ch)
                custom_m3u8 = SITE_URL + 'api/other/playlist.m3u8?uri=' + link.m3u8
            else:
                title = clean_title(ch)
                custom_m3u8 = SITE_URL + 'api/playlist.m3u8?uri=' + link.m3u8
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
    fsock = open("lista.m3u8", "rb")
    return HttpResponse(fsock, content_type='text')
