from django.contrib import admin

# Register your models here.
from app.models import Channel, Link, Type

admin.site.register(Channel)
admin.site.register(Link)
admin.site.register(Type)
