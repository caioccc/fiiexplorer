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


class FundoFilter(django_filters.FilterSet):
    class Meta:
        model = Fundo
        fields = {
            'preco': ['lte'],
            'oscilacao_dia': ['lte', 'gte'],
            'liquidez': ['gte'],
            'ultimo_rendimento': ['gte'],
            'dy': ['gte'],
            'rentabilidade_mes': ['gte'],
            'num_cotas_emitidas': ['gte'],
            # 'vi_cota': ['lt', 'gt'],
            'tipo_gestao': ['iexact'],
            'mandato': ['exact'],
            'segmento': ['iexact'],
            'taxa_adm': ['lte'],
            'yd_12_p': ['gte'],
            'num_ativos': ['gte'],
            'num_estados': ['gte'],
        }
