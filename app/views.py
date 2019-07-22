from datetime import datetime
from threading import Thread

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, FormView
from django.views.generic import TemplateView

from app.forms import FundoFilter
from app.miner.explorer import syncFunds, mineData
from app.models import Fundo


class IndexView(LoginRequiredMixin, FormView):
    login_url = '/admin/login'
    template_name = 'list_funds.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        fundos = Fundo.objects.all()
        fundo_filter = FundoFilter(self.request.GET, queryset=fundos)
        kwargs['fundos'] = fundo_filter
        return kwargs

    def get(self, request, *args, **kwargs):
        # Thread(target=syncFunds).start()
        return super(IndexView, self).get(request, *args, **kwargs)

    # def get_queryset(self):
    # q_dy = float(0.0)
    # if 'q_dy' in self.request.GET:
    #     q_dy = float(str(self.request.GET['q_dy']).replace('_', ''))

    # arr = []

    # for fundo in fundos:
    #     new_fund = fundo
    #     if float(new_fund.dy) <= q_dy:
    #         continue
    #     new_fund.preco = float(new_fund.preco)
    #     new_fund.oscilacao_dia = float(new_fund.oscilacao_dia)
    #     new_fund.liquidez = int(new_fund.liquidez)
    #
    #     new_fund.dy = "{0:.2f}".format(float(new_fund.dy))
    #     # new_fund.pl = float(new_fund.pl)
    #     new_fund.rentabilidade_mes = float(new_fund.rentabilidade_mes)
    #     # new_fund.data_construcao_fundo = datetime.strptime(str(new_fund.data_construcao_fundo), '%d de %B de %Y')
    #     new_fund.num_cotas_emitidas = int(new_fund.num_cotas_emitidas)
    #     if 'n/a' in new_fund.vi_cota.lower():
    #         new_fund.vi_cota = '0'
    #     if len(new_fund.vi_cota.split('.')) > 2:
    #         new_fund.vi_cota = float(new_fund.vi_cota.replace('.', '', 1))
    #     else:
    #         new_fund.vi_cota = float(new_fund.vi_cota)
    #     new_fund.yd_12_p = float(new_fund.yd_12_p)
    #     new_fund.num_ativos = int(new_fund.num_ativos)
    #     new_fund.num_estados = int(new_fund.num_estados)
    #     arr.append(new_fund)
    # return arr
