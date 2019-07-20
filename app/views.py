from threading import Thread

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from app.miner.explorer import syncFunds, mineData


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        Thread(target=mineData).start()
        # Thread(target=syncFunds).start()
        return super(IndexView, self).get(request, *args, **kwargs)
