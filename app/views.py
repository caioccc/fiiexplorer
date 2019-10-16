from datetime import datetime
from threading import Thread

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, FormView, RedirectView, DetailView
from django.views.generic import TemplateView

from app.forms import FundoFilter
from app.miner.explorer import syncFunds, mineData, Settings
from app.miner.miner_fiis import get_info_fii
from app.models import Fundo, Historico, InfoFundo, Carteira

import logging

logging.basicConfig(level=logging.DEBUG)


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = '/admin/login'

    def get_context_data(self, **kwargs):
        fundos = Fundo.objects.all()
        users = User.objects.all()
        settings = Settings.getInstance()
        bd = float((len(fundos) + len(users) + len(Historico.objects.all()) + len(Session.objects.all()) + 16)) / float(
            10000)
        kwargs['bd'] = bd
        kwargs['fundos'] = fundos
        kwargs['users'] = users
        kwargs['running'] = settings.get_running()
        print(kwargs['running'])
        return kwargs


class FundoDetailView(DetailView):
    template_name = 'view_fund.html'
    model = Fundo
    pk_url_kwarg = 'pk'
    context_object_name = 'fundo'


class GetInfoFundos(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        settings = Settings.getInstance()
        try:
            settings.infosThread.start()
        except (Exception,):
            logging.error('Thread nao pode ser iniciada novamente')
        return redirect('/')


class FundosListView(LoginRequiredMixin, FormView):
    login_url = '/admin/login'
    template_name = 'list_funds.html'
    success_url = '/fundos/'

    def get_context_data(self, **kwargs):
        fundos = Fundo.objects.all()
        fundo_filter = FundoFilter(self.request.GET, queryset=fundos)
        kwargs['fundos'] = fundo_filter
        return kwargs

    def get(self, request, *args, **kwargs):
        return super(FundosListView, self).get(request, *args, **kwargs)


class FilterFundoSelect(LoginRequiredMixin, TemplateView):
    template_name = 'list_funds_best.html'

    def calc_rent_cota_total(self, fundo):
        infos = fundo.infofundo_set.all()
        if len(infos) > 0:
            vf = float(infos[0].close)
            vi = float(infos[len(infos) - 1].close)
            rent = ((vf / vi) - 1) * 100
            return rent
        else:
            return -1

    def mount_dict(self, fundos):
        dic = {}
        for fundo in fundos:
            dic[fundo.pk] = self.calc_rent_cota_total(fundo=fundo)
        ordered = sorted(dic.iteritems(), key=lambda x: x[1])
        return ordered

    def get_context_data(self, **kwargs):
        qs = 10
        if 'qs' in self.request.GET:
            qs = int(self.request.GET['qs'])
        print('QS: ' + str(qs))
        fundos = Fundo.objects.all()
        ordered = self.mount_dict(fundos)
        pks = [x[0] for x in ordered if float(x[1]) > qs]
        kwargs['fundos'] = fundos.filter(pk__in=pks)
        return kwargs

    def get(self, request, *args, **kwargs):
        return super(FilterFundoSelect, self).get(request, *args, **kwargs)


class SetOnlineRedirect(LoginRequiredMixin, RedirectView):
    url = '/'
    login_url = '/admin/login'

    def get(self, request, *args, **kwargs):
        settings = Settings.getInstance()
        val = not settings.get_running()
        print('set val', val)
        settings.set_running(val)
        if settings.get_running():
            try:
                settings.minerThread.start()
                settings.thread.start()
            except (Exception,):
                logging.error('Thread nao pode ser iniciada novamente')
        return super(SetOnlineRedirect, self).get(request, *args, **kwargs)


class CarteiraList(ListView):
    template_name = 'carteiras_list.html'
    model = Carteira
    ordering = '-created_at'
    context_object_name = 'carteiras'


class ViewCarteira(DetailView):
    template_name = 'view_carteira.html'
    model = Carteira
    context_object_name = 'carteira'
