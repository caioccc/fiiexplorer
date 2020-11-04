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
from django.urls import path
from django.contrib.auth import views as auth_views
from app.views import TopCanaisView, ViewChannel, CanaisMaxView, CollectTopCanais, CollectCanaisMax, CollectFilmes, \
    FilmesView, ViewFilm, SeriesView, CollectSeries, ViewSerie, CollectSerie, CollectCanal, get_json, generate_m3u, \
    get_ts, get_other_m3u, generate_lista, get_lista_gen

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CanaisMaxView.as_view(), name='index'),
    path('topcanais/', TopCanaisView.as_view(), name='topcanais'),
    path('canaismax/', CanaisMaxView.as_view(), name='canaismax'),
    path('filmes/', FilmesView.as_view(), name='filmes'),
    path('series/', SeriesView.as_view(), name='series'),
    path('view-film/<int:pk>', ViewFilm.as_view(), name='view-film'),
    path('view-channel/<int:pk>', ViewChannel.as_view(), name='view-channel'),
    path('view-serie/<int:pk>', ViewSerie.as_view(), name='view-serie'),
    path('collect-filmes/', CollectFilmes.as_view(), name='collect-filmes'),
    path('collect/', CollectTopCanais.as_view(), name='collect'),
    path('collect-canaismax/', CollectCanaisMax.as_view(), name='collect-canaismax'),
    path('collect-series/', CollectSeries.as_view(), name='collect-series'),
    path('collect-serie/<int:pk>', CollectSerie.as_view(), name='collect-serie'),
    path('collect-canal/<int:pk>', CollectCanal.as_view(), name='collect-canal'),
    path('logout/', auth_views.logout_then_login, name='logout'),

    path('get-json/', get_json, name='get-json'),
    path('api/playlist.m3u8', generate_m3u, name='generate-m3u'),
    path('ts', get_ts, name='get-ts'),
    path('api/other/playlist.m3u8', get_other_m3u, name='get-other-m3u'),
    path('generate-list', generate_lista, name='generate-list'),
    path('lista.m3u8', get_lista_gen, name='get-lista-gen'),

]
