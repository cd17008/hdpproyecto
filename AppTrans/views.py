from django.shortcuts import render, redirect
from AppTrans.models import Motorista, RegistroLlegada, UnidadTransporte, PuntoControl
from AppTrans.forms import FormularioRegistro, FormularioUnidades

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
	#unidad = UnidadTransporte.objects.get(id=id)
	if request.method == 'POST':
		formulario = FormularioRegistro(request.POST)
		if formulario.is_valid():
			formulario.save()
		return redirect('home')
	else:
		formulario = FormularioRegistro()

	return render(request, 'crearRegistro.html', {'formulario':formulario})

def verDetalleRegistro(request, id):
	registro = RegistroLlegada.objects.get(id=id)
	return render(request, 'verDetalleRegistro.html', {'registro':registro})

def asignarMotorista(request, id):
	motoristas = Motorista.objects.all()
	unidad = UnidadTransporte.objects.get(id=id)
	return render(request, 'asignarMotorista.html', {'motoristas':motoristas}, {'unidad':unidad}) 

def seleccionarUnidad(request):
	if request.method == 'POST':
		formulario = FormularioUnidades(request.POST)
		if formulario.is_valid():
			formulario.save()
		return redirect('crearRegistro')
	else:
		formulario = FormularioUnidades()

	return render(request, 'seleccionarUnidad.html', {'formulario':formulario})

def consultarResponsables(request):
	responsables=ResponsablePunto.objects.all()
	return render(request, 'consultarResponsables.html', {'responsables':responsables})