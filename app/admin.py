from django.contrib import admin

# Register your models here.
from app.models import Channel, Link, Site, CategoryChannel, Url, Filme, Episodio, Temporada, Serie


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
admin.site.register(Filme)
admin.site.register(Url)
admin.site.register(Serie)
admin.site.register(Temporada)
admin.site.register(Episodio)


class AdminCanal(admin.ModelAdmin):
    list_display = ['id', 'name', 'group_title', 'status']
    search_fields = ['name', 'group_title', 'status']
    list_filter = ['status']

    def change_status_to_one(self, request, queryset):
        queryset.update(status=1)


class AdminGrupo(admin.ModelAdmin):
    pass
