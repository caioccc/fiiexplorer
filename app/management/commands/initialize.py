from django.core.management.base import BaseCommand, CommandError
from app.models import *
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Script para inicializar Template Base'

    def handle(self, *args, **options):
        try:
            site = Site()
            site.name = 'canaismax'
            site.url = 'https://canaismax.com/'
            site.save()
            cat1 = CategoryChannel()
            cat1.name = 'TV AO VIVO'
            cat1.url = 'https://canaismax.com/tvaovivo/'
            cat1.path = 'tvaovivo/'
            cat1.site = site
            cat1.save()

            site2 = Site()
            site2.name = 'topcanais'
            site2.url = 'https://topcanais.com/'
            site2.save()
            cat21 = CategoryChannel()
            cat21.name = 'Esportes'
            cat21.url = 'https://topcanais.com/esportes/'
            cat21.path = 'esportes/'
            cat21.site = site2
            cat21.pages = 2
            cat21.save()
            cat22 = CategoryChannel()
            cat22.name = 'Variedades'
            cat22.url = 'https://topcanais.com/variedades/'
            cat22.path = 'variedades/'
            cat22.site = site2
            cat22.save()
            cat23 = CategoryChannel()
            cat23.name = 'Documentarios'
            cat23.url = 'https://topcanais.com/documentarios/'
            cat23.path = 'documentarios/'
            cat23.site = site2
            cat23.pages = 2
            cat23.save()
            cat24 = CategoryChannel()
            cat24.name = 'Filmes e Series'
            cat24.url = 'https://topcanais.com/filmes-e-series/'
            cat24.path = 'filmes-e-series/'
            cat24.site = site2
            cat24.pages = 4
            cat24.save()

            site3 = Site()
            site3.name = 'filmes'
            site3.url = 'https://canaismax.com/'
            site3.save()
            cat31 = CategoryChannel()
            cat31.name = 'filmes'
            cat31.url = 'https://canaismax.com/filmes'
            cat31.path = 'filmes/'
            cat31.site = site3
            cat31.pages = 48
            cat31.save()

            site4 = Site()
            site4.name = 'series'
            site4.url = 'https://canaismax.com/'
            site4.save()
            cat41 = CategoryChannel()
            cat41.name = 'series'
            cat41.url = 'https://canaismax.com/series'
            cat41.path = 'series/'
            cat41.site = site4
            cat41.pages = 26
            cat41.save()

        except (Exception,):
            raise CommandError('Erro ao inicializar Models')
        self.stdout.write(self.style.SUCCESS('Successfully created sites and categories'))
