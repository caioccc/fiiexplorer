import logging
from threading import Thread

import requests
from bs4 import BeautifulSoup
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, DetailView, TemplateView

from app.miner.explorer import mineTopCanais, mineCanaisMax
from app.models import Channel, Link, Site

logging.basicConfig(level=logging.DEBUG)


class CollectTopCanais(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        site = Site.objects.get(name='topcanais')
        site.done = False
        site.save()
        Thread(target=mineTopCanais).start()
        return redirect('/')


class CollectCanaisMax(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        site = Site.objects.get(name='canaismax')
        site.done = False
        site.save()
        Thread(target=mineCanaisMax).start()
        return redirect('/')


class TopCanaisView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    login_url = '/admin/login/'
    model = Channel
    context_object_name = 'canais'

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['site'] = 'topcanais'
        return super(TopCanaisView, self).get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        if 'q' in self.request.GET:
            return Channel.objects.filter(title__icontains=self.request.GET['q'], category__site__name='topcanais')
        return Channel.objects.filter(category__site__name='topcanais')


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
            return Channel.objects.filter(title__icontains=self.request.GET['q'])
        return Channel.objects.all()


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


class CanaisMaxView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    login_url = '/admin/login/'
    model = Channel
    context_object_name = 'canais'

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['site'] = 'canaismax'
        return super(CanaisMaxView, self).get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        if 'q' in self.request.GET:
            return Channel.objects.filter(title__icontains=self.request.GET['q'],
                                          category__site__name='canaismax')
        return Channel.objects.filter(category__site__name='canaismax')


@require_http_methods(["GET"])
def template_multi(request, pk):
    ch = Channel.objects.get(pk=pk)
    req = requests.get(ch.link_set.first().url)
    if req.status_code == 200:
        page = BeautifulSoup(req.text, 'html.parser')
        print(page)
    html_text = req.text
    return HttpResponse(html_text)
