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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from app.views import FundosListView, IndexView, SetOnlineRedirect, FundoDetailView, GetInfoFundos, FilterFundoSelect, \
    CarteiraList, ViewCarteira

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/login/$', auth_views.login),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^fundo/(?P<pk>[0-9]+)/$', FundoDetailView.as_view(), name="fundo-view"),
    url(r'^set-online-crawling/', SetOnlineRedirect.as_view(), name='set_online'),
    url(r'^fundos/$', FundosListView.as_view(), name='fundos-list'),
    url(r'^logout/', auth_views.logout, name='logout'),
    url(r'^get-infos/$', GetInfoFundos.as_view(), name='infos'),
    url(r'^filter-bests/$', FilterFundoSelect.as_view(), name='filter-bests'),
    url(r'^carteiras/$', CarteiraList.as_view(), name='carteiras-list'),
    url(r'^carteiras/(?P<pk>[0-9]+)/$', ViewCarteira.as_view(), name="carteira-view"),
]
