from datetime import datetime
from threading import Thread

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, FormView, RedirectView
from django.views.generic import TemplateView

from app.forms import FundoFilter
from app.miner.explorer import syncFunds, mineData, Settings
from app.models import Fundo, Historico

import logging

logging.basicConfig(level=logging.DEBUG)


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = '/admin/login'

    def get_context_data(self, **kwargs):
        fundos = Fundo.objects.all()
        users = User.objects.all()
        settings = Settings.getInstance()
        mined = settings.get_mined()
        bd = float((len(fundos) + len(users) + len(Historico.objects.all()) + len(Session.objects.all()) + 16)) / float(
            10000)
        kwargs['bd'] = bd
        kwargs['fundos'] = fundos
        kwargs['users'] = users
        kwargs['mined'] = mined
        kwargs['running'] = settings.get_running()
        print(kwargs['running'])
        return kwargs


class FundosListView(LoginRequiredMixin, FormView):
    login_url = '/admin/login'
    template_name = 'list_funds.html'
    success_url = '/fundos'

    def get_context_data(self, **kwargs):
        fundos = Fundo.objects.all()
        fundo_filter = FundoFilter(self.request.GET, queryset=fundos)
        kwargs['fundos'] = fundo_filter
        return kwargs

    def get(self, request, *args, **kwargs):
        return super(FundosListView, self).get(request, *args, **kwargs)


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
