from django.core.management.base import BaseCommand, CommandError

from app.models import *


class Command(BaseCommand):
    help = 'Script para deletar Template Base'

    def handle(self, *args, **options):
        try:
            Site.objects.all().delete()
            CategoryChannel.objects.all().delete()
            Channel.objects.all().delete()
            Link.objects.all().delete()
            Filme.objects.all().delete()
            Url.objects.all().delete()
            User.objects.all().delete()
            Filme.objects.all().delete()
            Serie.objects.all().delete()
            Temporada.objects.all().delete()
            Episodio.objects.all().delete()
            LinkSerie.objects.all().delete()
        except (Exception,):
            raise CommandError('Erro ao deletar Models')
        self.stdout.write(self.style.SUCCESS('Successfully deleted'))
