from django.core.management.base import BaseCommand, CommandError
from app.models import *
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Script para deletar Template Base'

    def handle(self, *args, **options):
        try:
            Site.objects.all().delete()
            CategoryChannel.objects.all().delete()
            Channel.objects.all().delete()
            Link.objects.all().delete()
            users = User.objects.all().delete()
        except (Exception,):
            raise CommandError('Erro ao deletar Models')
        self.stdout.write(self.style.SUCCESS('Successfully deleted'))
