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
    name = models.CharField(max_length=255, blank=True, null=True, default='topcanais')
    url = models.URLField(blank=True, null=True, default='https://topcanais.com/')
    done = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "%s" % self.name


class CategoryChannel(TimeStamped):
    name = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    site = models.ForeignKey(Site, blank=True, null=True, on_delete=models.CASCADE)
    pages = models.IntegerField(blank=True, null=True, default=1)
    css_selector = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "%s" % self.name


class Channel(TimeStamped):
    title = models.CharField(max_length=255, blank=True, null=True)
    img_url = models.TextField(blank=True, null=True)
    category = models.ForeignKey(CategoryChannel, blank=True, null=True, on_delete=models.CASCADE)
    channel_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "%s" % self.title

    def __unicode__(self):
        return "%s" % self.title


class Link(TimeStamped):
    url = models.TextField(blank=True, null=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.url

    def __unicode__(self):
        return "%s" % self.url


class Filme(TimeStamped):
    title = models.CharField(max_length=255, blank=True, null=True)
    duracao = models.CharField(max_length=255, blank=True, null=True)
    img_url = models.TextField(blank=True, null=True)
    ano = models.CharField(max_length=255, blank=True, null=True)
    sinopse = models.TextField(blank=True, null=True)
    imdb = models.TextField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s" % self.title

    def __unicode__(self):
        return "%s" % self.title


class Url(TimeStamped):
    url = models.TextField(blank=True, null=True)
    filme = models.ForeignKey(Filme, blank=True, null=True, on_delete=models.CASCADE)
    data_id = models.TextField(blank=True, null=True)
    data_player = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s" % self.url

    def __unicode__(self):
        return "%s" % self.url


class Serie(TimeStamped):
    title = models.TextField(blank=True, null=True)
    imdb = models.TextField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)
    img_url = models.TextField(blank=True, null=True)
    temporadas = models.TextField(blank=True, null=True)
    sinopse = models.TextField(blank=True, null=True)
    episodios = models.TextField(blank=True, null=True)
    duracao = models.TextField(blank=True, null=True)
    ano = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s" % self.title

    def __unicode__(self):
        return "%s" % self.title


class Temporada(TimeStamped):
    serie = models.ForeignKey(Serie, blank=True, null=True, on_delete=models.CASCADE)
    num_seq = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.serie, self.num_seq)

    def __unicode__(self):
        return "%s %s" % (self.serie, self.num_seq)


class Episodio(TimeStamped):
    temporada = models.ForeignKey(Temporada, blank=True, null=True, on_delete=models.CASCADE)
    type = models.TextField(blank=True, null=True)
    img_url = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.temporada.serie, self.type)

    def __unicode__(self):
        return "%s %s" % (self.temporada.serie, self.type)


class LinkSerie(TimeStamped):
    url = models.TextField(blank=True, null=True)
    episodio = models.ForeignKey(Episodio, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.episodio

    def __unicode__(self):
        return "%s" % self.episodio
