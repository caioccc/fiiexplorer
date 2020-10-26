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
from app.views import CanaisView, collect_canais, ViewChannel, ViewLink, JogosView, collect_jogos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CanaisView.as_view(), name='index'),
    path('sports/', JogosView.as_view(), name='sports'),
    path('view-channel/<int:pk>', ViewChannel.as_view(), name='view-channel'),
    path('view-link/<int:pk>', ViewLink.as_view(), name='view-link'),
    path('collect/', collect_canais, name='collect'),
    path('collect-sports/', collect_jogos, name='collect-sports'),
    path('logout/', auth_views.logout_then_login, name='logout'),
]
