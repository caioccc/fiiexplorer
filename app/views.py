import datetime
import json
import logging
from threading import Thread

# Create your views here.
import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, TemplateView

from app.miner.explorer import mineTopCanais, mineCanaisMax, mineFilmes, mineSeries
from app.models import Channel, Site, Filme, Serie

logging.basicConfig(level=logging.DEBUG)


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


class TopCanaisView(LoginRequiredMixin, ListView):
    template_name = 'topcanais.html'
    login_url = '/admin/login/'
    model = Channel
    context_object_name = 'canais'

    def get_context_data(self, *, object_list=None, **kwargs):
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

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs = self.insert_context_data(**kwargs)
        return super(ViewChannel, self).get_context_data(object_list=object_list, **kwargs)

    def insert_context_data(self, **kwargs):
        channel_id = self.get_object().channel_id
        url = 'https://canaismax.com/api/canal/' + channel_id + '/' + str(get_date_now())
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

    def get_context_data(self, *, object_list=None, **kwargs):
        return super(CanaisMaxView, self).get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        if 'q' in self.request.GET:
            return Channel.objects.filter(title__icontains=self.request.GET['q'],
                                          category__site__name='canaismax')
        return Channel.objects.filter(category__site__name='canaismax')


def get_date_now():
    now = datetime.datetime.now()
    month = str("0") + str(now.month) if now.month < 10 else now.month
    day = now.day
    return '%s-%s-%s' % (now.year, month, day)
