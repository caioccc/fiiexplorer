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


class Type(TimeStamped):
    name = models.CharField(max_length=255, blank=True, null=True, default='Canais')

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "%s" % self.name


class Channel(TimeStamped):
    title = models.CharField(max_length=255, blank=True, null=True)
    img_url = models.URLField(blank=True, null=True)
    type = models.ForeignKey(Type, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.title

    def __unicode__(self):
        return "%s" % self.title


class Link(TimeStamped):
    url = models.URLField(blank=True, null=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.url

    def __unicode__(self):
        return "%s" % self.url
