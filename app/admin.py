from django.contrib import admin

# Register your models here.
from app.models import Channel, Link

admin.site.register(Channel)
admin.site.register(Link)
