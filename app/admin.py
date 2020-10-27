from django.contrib import admin

# Register your models here.
from app.models import Channel, Link, Site, CategoryChannel


class CategoryInline(admin.TabularInline):
    model = CategoryChannel


class SiteAdmin(admin.ModelAdmin):
    inlines = [CategoryInline, ]
    search_fields = ['name', 'url', ]
    list_display = ['name', 'id', 'url', ]


admin.site.register(Channel)
admin.site.register(Link)
admin.site.register(CategoryChannel)
admin.site.register(Site, SiteAdmin)
