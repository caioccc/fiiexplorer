# coding=utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class TimeStamped(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)


class Site(TimeStamped):
    nome = models.CharField(max_length=300, blank=True, null=True)
    done = models.BooleanField(default=False)


class Fundo(TimeStamped):
    nome = models.CharField(max_length=300, blank=True, null=True)
    sigla = models.CharField(max_length=300, blank=True, null=True)
    preco = models.FloatField(max_length=300, blank=True, null=True)
    oscilacao_dia = models.FloatField(max_length=300, blank=True, null=True, verbose_name='Oscilação do dia (%)')
    liquidez = models.IntegerField(max_length=300, blank=True, null=True)
    ultimo_rendimento = models.FloatField(max_length=300, blank=True, null=True, verbose_name='Último Rendimento (R$)')
    dy = models.FloatField(max_length=300, blank=True, null=True, verbose_name='DY (%)')
    pl = models.CharField(max_length=300, blank=True, null=True, verbose_name='Patrimônio Líquido')
    rentabilidade_mes = models.FloatField(max_length=300, blank=True, null=True,
                                          verbose_name='Rentabilidade no Mês (%)')
    descricao = models.TextField(blank=True, null=True)
    data_construcao_fundo = models.CharField(max_length=300, blank=True, null=True)
    num_cotas_emitidas = models.IntegerField(max_length=300, blank=True, null=True, verbose_name='Número de Cotas')
    vi_cota = models.FloatField(max_length=300, blank=True, null=True, verbose_name='Valor Inicial da Cota')
    tipo_gestao = models.CharField(max_length=300, blank=True, null=True, verbose_name='Tipo de Gestão')
    publico_alvo = models.CharField(max_length=300, blank=True, null=True, verbose_name='Público Alvo')
    mandato = models.CharField(max_length=300, blank=True, null=True)
    segmento = models.CharField(max_length=300, blank=True, null=True)
    prazo_duracao = models.CharField(max_length=300, blank=True, null=True, verbose_name='Prazo de Duração')
    taxa_adm = models.CharField(max_length=300, blank=True, null=True, verbose_name='Taxa de Admin.')
    yd_1 = models.FloatField(max_length=300, blank=True, null=True, verbose_name='DY 1 (R$)')
    yd_3 = models.FloatField(max_length=300, blank=True, null=True, verbose_name='DY 3 (R$)')
    yd_6 = models.FloatField(max_length=300, blank=True, null=True, verbose_name='DY 6 (R$)')
    yd_12 = models.FloatField(max_length=300, blank=True, null=True, verbose_name='DY 12 (R$)')
    yd_1_p = models.FloatField(max_length=300, blank=True, null=True, verbose_name='DY 1 (%)')
    yd_3_p = models.FloatField(max_length=300, blank=True, null=True, verbose_name='DY 3 (%)')
    yd_6_p = models.FloatField(max_length=300, blank=True, null=True, verbose_name='DY 6 (%)')
    yd_12_p = models.FloatField(max_length=300, blank=True, null=True, verbose_name='DY 12 (%)')
    num_ativos = models.IntegerField(max_length=300, blank=True, null=True, verbose_name='Número de Ativos')
    num_estados = models.IntegerField(max_length=300, blank=True, null=True, verbose_name='Número de Estados')
    url = models.URLField()

    def __str__(self):
        return "%s" % self.sigla

    def __unicode__(self):
        return "%s" % self.sigla


class Historico(TimeStamped):
    fund = models.ForeignKey(Fundo, blank=True, null=True, on_delete=models.CASCADE)
    preco = models.CharField(max_length=300, blank=True, null=True)
    oscilacao_dia = models.CharField(max_length=300, blank=True, null=True)
    liquidez = models.CharField(max_length=300, blank=True, null=True)
    ultimo_rendimento = models.CharField(max_length=300, blank=True, null=True)
    dy = models.CharField(max_length=300, blank=True, null=True)
    pl = models.CharField(max_length=300, blank=True, null=True)
    rentabilidade_mes = models.CharField(max_length=300, blank=True, null=True)
    yd_1 = models.CharField(max_length=300, blank=True, null=True)
    yd_3 = models.CharField(max_length=300, blank=True, null=True)
    yd_6 = models.CharField(max_length=300, blank=True, null=True)
    yd_12 = models.CharField(max_length=300, blank=True, null=True)
    yd_1_p = models.CharField(max_length=300, blank=True, null=True)
    yd_3_p = models.CharField(max_length=300, blank=True, null=True)
    yd_6_p = models.CharField(max_length=300, blank=True, null=True)
    yd_12_p = models.CharField(max_length=300, blank=True, null=True)
    num_ativos = models.CharField(max_length=300, blank=True, null=True)
    num_estados = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return "%s" % self.fund

    def __unicode__(self):
        return "%s" % self.fund


class InfoFundo(TimeStamped):
    fund = models.ForeignKey(Fundo, blank=True, null=True, on_delete=models.CASCADE)
    dy = models.CharField(max_length=300, blank=True, null=True)
    data_pay = models.CharField(max_length=300, blank=True, null=True)
    rend = models.CharField(max_length=300, blank=True, null=True)
    data_base = models.CharField(max_length=300, blank=True, null=True)
    close = models.CharField(max_length=300, blank=True, null=True)
    rend_cota_mes = models.CharField(max_length=300, blank=True, null=True)


class Carteira(TimeStamped):
    nome = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return "%s" % self.nome

    def __unicode__(self):
        return "%s" % self.nome


class ItemFundo(TimeStamped):
    carteira = models.ForeignKey(Carteira, blank=True, null=True, on_delete=models.CASCADE)
    qtd = models.IntegerField(blank=True, null=True)
    fundo = models.ForeignKey(Fundo, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.fundo

    def __unicode__(self):
        return "%s" % self.fundo
