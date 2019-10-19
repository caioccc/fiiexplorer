#!/usr/bin/env python
# -*- coding: utf-8 -*-

import django_filters
from django import forms
from django.forms import ModelForm

from app.models import *


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'phone' or field_name == 'telefone':
                field.widget.attrs['class'] = 'form-control telefone'
            if field_name == 'numero' or field_name == 'number':
                field.widget.attrs['class'] = 'form-control numero'


class FormFundo(ModelForm, BaseForm):
    class Meta:
        model = Fundo
        fields = [
            'preco',
            'oscilacao_dia',
            'liquidez',
            'ultimo_rendimento',
            'dy',
            'pl',
            'rentabilidade_mes',
            'num_cotas_emitidas',
            'vi_cota',
            'tipo_gestao',
            'mandato',
            'segmento',
            'taxa_adm',
            'yd_12_p',
            'num_ativos',
            'num_estados',
        ]


MANDATO_CHOICES = (
    ('Desenvolvimento para Renda', 'Desenvolvimento para Renda'),
    ('Desenvolvimento para Venda', 'Desenvolvimento para Venda'),
    ('Renda', 'Renda'),
    ('Títulos e Valores Mobiliários', 'Títulos e Valores Mobiliários'),
    ('Híbrido', 'Híbrido')
)

GESTAO_CHOICES = (
    ('Ativa', 'Ativa'),
    ('Passiva', 'Passiva')
)

SEGMENTO_CHOICES = (
    ('Híbrido', 'Híbrido'),
    ('Hospital', 'Hospital'),
    ('Hotel', 'Hotel'),
    ('Lajes Corporativas', 'Lajes Corporativas'),
    ('Logística', 'Logística'),
    ('Outros', 'Outros'),
    ('Residencial', 'Residencial'),
    ('Shoppings', 'Shoppings'),
    ('Títulos e Val Mob', 'Títulos e Valores Mobiliários'),
)


class FundoFilter(django_filters.FilterSet):
    mandato = django_filters.MultipleChoiceFilter(choices=MANDATO_CHOICES, label='Mandato')
    tipo_gestao = django_filters.MultipleChoiceFilter(choices=GESTAO_CHOICES, label='Tipo de Gestão')
    preco = django_filters.RangeFilter(label='Preço', )
    segmento = django_filters.MultipleChoiceFilter(choices=SEGMENTO_CHOICES, label='Segmento')

    class Meta:
        model = Fundo
        fields = {
            'preco': ['exact'],
            'oscilacao_dia': ['gte'],
            'liquidez': ['gte'],
            'ultimo_rendimento': ['gte'],
            'dy': ['gte'],
            'rentabilidade_mes': ['gte'],
            'num_cotas_emitidas': ['gte'],
            # 'vi_cota': ['lt', 'gt'],
            'tipo_gestao': ['exact'],
            'mandato': ['exact'],
            'segmento': ['exact'],
            'taxa_adm': ['icontains'],
            'yd_12_p': ['gte'],
            'num_ativos': ['gte'],
            'num_estados': ['gte'],
        }
