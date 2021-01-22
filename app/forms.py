#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.forms import SelectMultiple

from app.models import Channel


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'phone' or field_name == 'telefone':
                field.widget.attrs['class'] = 'form-control telefone'
            if field_name == 'numero' or field_name == 'number':
                field.widget.attrs['class'] = 'form-control numero'


class SelectMulticanais(forms.Form):
    channel = forms.ModelMultipleChoiceField(queryset=Channel.objects.filter(category__site__name='multicanais',link__m3u8__icontains='.m3u8').distinct(), widget=SelectMultiple(attrs={'size': 30}))
