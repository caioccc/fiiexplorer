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
from app.views import TopCanaisView, ViewChannel, ViewLink, JogosView, template_multi, \
    CanaisMaxView, CollectTopCanais, CollectCanaisMax, CollectFilmes, FilmesView, ViewFilm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TopCanaisView.as_view(), name='topcanais'),
    path('canaismax/', CanaisMaxView.as_view(), name='canaismax'),
    path('view-film/<int:pk>', ViewFilm.as_view(), name='view-film'),
    path('view-channel/<int:pk>', ViewChannel.as_view(), name='view-channel'),
    path('view-link/<int:pk>', ViewLink.as_view(), name='view-link'),
    path('collect-filmes/', CollectFilmes.as_view(), name='collect-filmes'),
    path('filmes/', FilmesView.as_view(), name='filmes'),
    path('collect/', CollectTopCanais.as_view(), name='collect'),
    path('collect-canaismax/', CollectCanaisMax.as_view(), name='collect-canaismax'),
    path('logout/', auth_views.logout_then_login, name='logout'),

    path('template/<int:pk>', template_multi, name='template')
]
