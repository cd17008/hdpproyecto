"""Proyecto_G14 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from AppTrans import views

from django.views.generic.base import TemplateView
from django.contrib.auth.views import login

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^home/$', views.home, name='home'),
    url(r'^home/consultarPuntos/$', views.consultarPuntos),
    url(r'^home/consultarUnidades/$', views.consultarUnidades, name='consultarUnidades'),
    url(r'^home/seleccionarUnidad/$', views.seleccionarUnidad, name='seleccionarUnidad'),
    url(r'^home/consultarUnidades/(?P<id>\d+)/$', views.consultarUnidades, name='consultarUnidades'),
    url(r'^home/consultarRegistros/$', views.consultarRegistros),
    url(r'^crearRegistro/$', views.crearRegistro, name='crearRegistro'),
    url(r'^consultarMotoristas/$', views.consultarMotoristas, name='consultarMotoristas'),
    url(r'^home/consultarUnidades/(?P<id>\d+)/crearRegistro$', views.crearRegistro),
    url(r'^verDetalleRegistro/(?P<id>\d+)/$', views.verDetalleRegistro, name='verDetalleRegistro'),
    url(r'^asignarMotorista/(?P<id>\d+)/$', views.asignarMotorista, name='asignarMotorista'),
    url(r'^consultarResponsables/$', views.consultarResponsables, name='consultarResponsables'),
    url(r'^home/crearPuntos/$', views.crearPuntos, name='crearPuntos'),
    url(r'^accounts/$', include('django.contrib.auth.urls')),
   url(r'^$',login, {'template_name':'index.html'},name='login'),
]
