from django.shortcuts import render, redirect
from django.http import HttpResponse
from transporte.models import Motorista, RegistroLlegada, UnidadTransporte, PuntoControl
from transporte.forms import FormRegistroLlegada

# Create your views here.

def home(request):
	return render(request, 'home.html');

def consultarMotoristas(request):
	motoristas=Motorista.objects.all()
	return render(request, 'consultarMotoristas.html', {'motoristas': motoristas})

def consultarPuntos(request):
	puntos=PuntoControl.objects.all()
	return render(request, 'consultarPuntos.html', {'puntos':puntos})

def consultarUnidades(request):
	unidades=UnidadTransporte.objects.all()
	return render(request, 'consultarUnidades.html', {'unidades':unidades})

def consultarRegistros(request):
	registros=RegistroLlegada.objects.all()
	return render(request, 'consultarRegistros.html', {'registros':registros})

def crearRegistro(request):
	if request.method=='POST':
		formulario=FormRegistroLlegada(request.POST)
		if formulario.is_valid():
			formulario.save()
		return redirect('home')
	else:
		formulario=FormRegistroLlegada()

	return render(request, 'crearRegistro.html', {'formulario':formulario})