from __future__ import unicode_literals

from django.db import models


# Create your models here.
class TimeStamped(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)


class Fundo(TimeStamped):
    nome = models.CharField(max_length=300, blank=True, null=True)
    sigla = models.CharField(max_length=300, blank=True, null=True)
    preco = models.CharField(max_length=300, blank=True, null=True)
    oscilacao_dia = models.CharField(max_length=300, blank=True, null=True)
    liquidez = models.CharField(max_length=300, blank=True, null=True)
    ultimo_rendimento = models.CharField(max_length=300, blank=True, null=True)
    dy = models.CharField(max_length=300, blank=True, null=True)
    pl = models.CharField(max_length=300, blank=True, null=True)
    rentabilidade_mes = models.CharField(max_length=300, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    data_construcao_fundo = models.CharField(max_length=300, blank=True, null=True)
    num_cotas_emitidas = models.CharField(max_length=300, blank=True, null=True)
    vi_cota = models.CharField(max_length=300, blank=True, null=True)
    tipo_gestao = models.CharField(max_length=300, blank=True, null=True)
    publico_alvo = models.CharField(max_length=300, blank=True, null=True)
    mandato = models.CharField(max_length=300, blank=True, null=True)
    segmento = models.CharField(max_length=300, blank=True, null=True)
    prazo_duracao = models.CharField(max_length=300, blank=True, null=True)
    taxa_adm = models.CharField(max_length=300, blank=True, null=True)
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
