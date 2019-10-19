from django.contrib import admin

# Register your models here.
from app.models import Historico, Fundo, Site, InfoFundo, ItemFundo, Carteira


class HistoricoInline(admin.TabularInline):
    model = Historico


class FundoAdmin(admin.ModelAdmin):
    search_fields = (
        'sigla',
    )
    list_filter = ('segmento', 'mandato', 'publico_alvo')
    inlines = [
        HistoricoInline,
    ]
    list_display = (
        'sigla', 'id', 'nome', 'preco', 'oscilacao_dia', 'liquidez', 'ultimo_rendimento', 'dy', 'rentabilidade_mes',
        'segmento', 'mandato', 'publico_alvo',
        'url', 'qtd_historico', 'created_at')

    def qtd_historico(self, obj):
        return len(obj.historico_set.all())


class HistoricoAdmin(admin.ModelAdmin):
    list_display = ('fund', 'id', 'preco', 'oscilacao_dia', 'liquidez', 'ultimo_rendimento', 'dy')


class InfoFundoAdmin(admin.ModelAdmin):
    list_filter = ('fund', 'data_pay',)
    search_fields = ['data_pay']
    list_display = ('fund', 'id', 'dy', 'rend', 'data_pay', 'data_base', 'close', 'rend_cota_mes')


class ItemFundoInline(admin.TabularInline):
    model = ItemFundo


class ItemFundoAdmin(admin.ModelAdmin):
    list_filter = ('carteira',)
    search_fields = ['fundo', 'carteira']
    list_display = ('carteira', 'id', 'fundo', 'qtd',)


class CarteiraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id', 'qtd_fundos')
    inlines = [ItemFundoInline, ]

    def qtd_fundos(self, obj):
        return len(obj.itemfundo_set.all())


admin.site.register(Fundo, FundoAdmin)
admin.site.register(Historico, HistoricoAdmin)
admin.site.register(Site)
admin.site.register(InfoFundo, InfoFundoAdmin)
admin.site.register(ItemFundo, ItemFundoAdmin)
admin.site.register(Carteira, CarteiraAdmin)
