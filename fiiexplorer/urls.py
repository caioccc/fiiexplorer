"""fiiexplorer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from app.views.AoVivoGratisView import AoVivoGratisView, ViewChannelAoVivoGratis, playlist_m3u8_aovivogratis, \
    get_ts_aovivogratis, CollectAllAoVivoGratis, GetListaAoVivoGratis, SnifferAoVivoGratis
from app.views.CanaisMaxView import CanaisMaxView, CollectAllCanaisMax, ViewChannelCanaisMax, CollectChannelCanaisMax, \
    playlist_m3u8_canaismax, playlist_other_m3u8_canaismax, get_ts_canaismax, get_lista_canaismax
from app.views.FilmeView import CollectFilmesCanaisMax, ViewFilmCanaisMax, FilmesView, gen_lista_filmes_canaismax, \
    get_ts_filmes_canaismax, playlist_m3u8_filmes_canaismax, CollectFilmeOneCanaisMax
from app.views.MultiCanaisView import CollectChannelMultiCanais, CollectAllMultiCanais, MultiCanaisView, \
    ViewChannelMultiCanais, playlist_m3u8_multicanais, get_ts_multicanais, gen_lista_multicanais
from app.views.SerieView import CollectSeries, CollectSerie, ViewSerie, SeriesView, playlist_m3u8_series_canaismax, \
    get_ts_series_canaismax, gen_lista_series_canaismax
from app.views.TopCanaisView import CollectAllTopCanais, TopCanaisView, ViewChannelTopCanais, CollectChannelTopCanais, \
    playlist_m3u8_topcanais, playlist_other_m3u8_topcanais, get_lista_topcanais, get_ts_topcanais

urlpatterns = [
    path('admin/', admin.site.urls),

    path('collect-channel-multicanais/<int:pk>', CollectChannelMultiCanais.as_view(),
         name='collect-channel-multicanais'),
    path('collect-multicanais/', CollectAllMultiCanais.as_view(), name='collect-multicanais'),
    path('', MultiCanaisView.as_view(), name='multicanais'),
    path('multicanais/', MultiCanaisView.as_view(), name='multicanais'),
    path('multicanais/<int:pk>', ViewChannelMultiCanais.as_view(), name='view-channel-multicanais'),
    path('api/multi/playlist.m3u8', playlist_m3u8_multicanais, name='playlist-m3u8-multicanais'),
    path('api/multi/ts', get_ts_multicanais, name='get-ts-multicanais'),
    path('lista-multicanais.m3u8', gen_lista_multicanais, name='gen-lista-multicanais'),

    path('collect-channel-canaismax/<int:pk>', CollectChannelCanaisMax.as_view(), name='collect-channel-canaismax'),
    path('collect-canaismax/', CollectAllCanaisMax.as_view(), name='collect-canaismax'),
    path('canaismax/', CanaisMaxView.as_view(), name='canaismax'),
    path('canaismax/<int:pk>', ViewChannelCanaisMax.as_view(), name='view-channel-canaismax'),
    path('api/max/playlist.m3u8', playlist_m3u8_canaismax, name='playlist-m3u8-canaismax'),
    path('api/max/other/playlist.m3u8', playlist_other_m3u8_canaismax, name='playlist-other-m3u8-canaismax'),
    path('api/max/ts', get_ts_canaismax, name='get-ts-canaismax'),
    path('lista-canaismax.m3u8', get_lista_canaismax, name='get-lista-canaismax'),

    path('collect-topcanais/', CollectAllTopCanais.as_view(), name='collect-topcanais'),
    path('collect-channel-topcanais/<int:pk>', CollectChannelTopCanais.as_view(), name='collect-channel-topcanais'),
    path('topcanais/', TopCanaisView.as_view(), name='topcanais'),
    path('topcanais/<int:pk>', ViewChannelTopCanais.as_view(), name='view-channel-topcanais'),
    path('api/topcanais/playlist.m3u8', playlist_m3u8_topcanais, name='playlist-m3u8-topcanais'),
    path('api/topcanais/other/playlist.m3u8', playlist_other_m3u8_topcanais, name='playlist-other-m3u8-topcanais'),
    path('api/topcanais/ts', get_ts_topcanais, name='get-ts-topcanais'),
    path('lista-topcanais.m3u8', get_lista_topcanais, name='get-lista-topcanais'),

    path('filmes/', FilmesView.as_view(), name='filmes'),
    path('collect-film/canaismax/<int:pk>', CollectFilmeOneCanaisMax.as_view(), name='collect-film-canaismax'),
    path('collect-filmes/', CollectFilmesCanaisMax.as_view(), name='collect-filmes-canaismax'),
    path('view-film/<int:pk>', ViewFilmCanaisMax.as_view(), name='view-film'),
    path('api/filmes/canaismax/playlist.m3u8', playlist_m3u8_filmes_canaismax, name='m3u8-filmes-canaismax'),
    path('api/filmes/canaismax/ts', get_ts_filmes_canaismax, name='ts-filmes-canaismax'),
    path('filmes-canaismax.m3u8', gen_lista_filmes_canaismax, name='gen-filmes-canaismax'),

    path('series/', SeriesView.as_view(), name='series'),
    path('series/<int:pk>', ViewSerie.as_view(), name='view-serie'),
    path('collect-series/', CollectSeries.as_view(), name='collect-series'),
    path('collect-serie/<int:pk>', CollectSerie.as_view(), name='collect-serie'),
    path('api/series/canaismax/playlist.m3u8', playlist_m3u8_series_canaismax, name='m3u8-series-canaismax'),
    path('api/series/canaismax/ts', get_ts_series_canaismax, name='ts-series-canaismax'),
    path('series-canaismax.m3u8', gen_lista_series_canaismax, name='gen-series-canaismax'),

    path('logout/', auth_views.logout_then_login, name='logout'),

    path('collect-aovivogratis/', CollectAllAoVivoGratis.as_view(), name='collect-aovivogratis'),
    path('run-sniffer/aovivogratis/', SnifferAoVivoGratis.as_view(), name='sniffer-aovivogratis'),
    path('aovivogratis/', AoVivoGratisView.as_view(), name='aovivogratis'),
    path('aovivogratis/<int:pk>', ViewChannelAoVivoGratis.as_view(), name='view-channel-aovivogratis'),
    path('api/aovivogratis/playlist.m3u8', playlist_m3u8_aovivogratis, name='playlist-m3u8-aovivogratis'),
    path('api/aovivogratis/ts', get_ts_aovivogratis, name='get-ts-aovivogratis'),
    path('lista-aovivogratis.m3u8', GetListaAoVivoGratis.as_view(), name='lista-aovivogratis')

]
