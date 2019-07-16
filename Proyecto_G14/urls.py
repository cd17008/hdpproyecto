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
from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^home/$', views.home, name='home'),
    url(r'^registrarUsuario/$', views.registrarUsuario.as_view(), name='registrarUsuario'),
    url(r'^home/consultarPuntos/$', views.consultarPuntos, name='consultarPuntos'),
    url(r'^home/consultarUnidades/$', views.consultarUnidades, name='consultarUnidades'),
    url(r'^home/consultarRegistros/$', views.consultarRegistros, name='consultarRegistros'),
    url(r'^home/consultarMotoristas/$', views.consultarMotoristas, name='consultarMotoristas'),
    url(r'^home/consultarResponsables/$', views.consultarResponsables, name='consultarResponsables'),
    url(r'^logout/', logout_then_login, name='logout' ),
    url(r'^home/crearRegistro/$', views.crearRegistro, name='crearRegistro'),
    url(r'^crearMotorista/$', views.crearMotorista, name='crearMotorista'),
    url(r'^crearUnidad/$', views.crearUnidad, name='crearUnidad'),
    url(r'^crearResponsable/$', views.crearResponsable, name='crearResponsable'),
    url(r'^crearPuntos/$', views.crearPuntos, name='crearPuntos'),

    url(r'^verDetalleRegistro/(?P<id_registro>\d+)/$', views.verDetalleRegistro, name='verDetalleRegistro'),
    url(r'^verDetalleResponsable/(?P<id_responsable>\d+)/$', views.verDetalleResponsable, name='verDetalleResponsable'),
    url(r'^verDetalleMotorista/(?P<id_motorista>\d+)/$', views.verDetalleMotorista, name='verDetalleMotorista'),
    url(r'^verDetalleUnidad/(?P<id_unidad>\d+)/$', views.verDetalleUnidad, name='verDetalleUnidad'),
    
    url(r'^cambiarMotorista/(?P<id_unidad>\d+)/$', views.cambiarMotorista, name='cambiarMotorista'),
    url(r'^editarPunto/(?P<id_punto>\d+)/$', views.editarPunto, name='editarPunto'),
    
    url(r'^eliminarUnidad/(?P<id_unidad>\d+)/$', views.eliminarUnidad, name='eliminarUnidad'),
    url(r'^eliminarMotorista/(?P<id_motorista>\d+)/$', views.eliminarMotorista, name='eliminarMotorista'),
    url(r'^eliminarResponsable/(?P<id_responsable>\d+)/$', views.eliminarResponsable, name='eliminarResponsable'),
    
   # url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$',login, {'template_name':'index.html'},name='login'),
]
