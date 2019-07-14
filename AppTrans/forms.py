from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from AppTrans.models import RegistroLlegada, Motorista, UnidadTransporte, PuntoControl, ResponsablePunto

#Formulario para crear usuario
class UsuarioForm(UserCreationForm):
	class Meta:
		model = User

		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
		]

		labels = {
			'username':'Nombre de Usuario',
			'first_name':'Nombre(s)',
			'last_name':'Apellido(s)',
			'email':'Correo Electrónico',
		}

#Formulario para crear registro de llegada
class RegistroForm(forms.ModelForm):
	class Meta:
		model = RegistroLlegada

		fields = [
			'cod_registro',
			'unidad',
			'punto',
			#'responsable',
			'num_pasajeros',
			'cant_dinero',
		]

		labels = {
			'cod_registro':'Código del Registro',
			'unidad':'Unidad de Transporte',
			'punto':'Punto de Control',
			#'responsable':'Responsable de Punto',
			'num_pasajeros':'Cantidad de pasajeros (opcional)',
			'cant_dinero':'Cantidad de dinero',
		}

		widgets = {
			'cod_registro':forms.TextInput(attrs={'class':'form-control'}),
			'unidad':forms.Select(attrs={'class':'form-control'}),
			'punto':forms.Select(attrs={'class':'form-control'}),
			#'responsable':forms.Select(attrs={'class':'form-control'}),
			'num_pasajeros':forms.TextInput(attrs={'class':'form-control'}),
			'cant_dinero':forms.TextInput(attrs={'class':'form-control'}),
		}

#Formulario para registrar un nuevo motorista
class MotoristaForm(forms.ModelForm):
	class Meta:
		model = Motorista

		fields = [
			'cod_motorista',
			'dui',
			'nit',
			'nombres',
			'apellidos',
			'direccion',
		]

		labels = {
			'cod_motorista':'Código',
			'dui':'DUI',
			'nit':'NIT',
			'nombres':'Nombre(s)',
			'apellidos':'Apellido(s)',
			'direccion':'Direccion',
		}

		widgets = {
			'cod_motorista':forms.TextInput(attrs={'class':'form-control'}),
			'dui':forms.TextInput(attrs={'class':'form-control'}),
			'nit':forms.TextInput(attrs={'class':'form-control'}),
			'nombres':forms.TextInput(attrs={'class':'form-control'}),
			'apellidos':forms.TextInput(attrs={'class':'form-control'}),
			'direccion':forms.TextInput(attrs={'class':'form-control'}),
		}

class ResponsableForm(forms.ModelForm):
	class Meta:
		model = ResponsablePunto

		fields = [
			'cod_responsable',
			'dui',
			'nit',
			'nombres',
			'apellidos',
			'direccion',
		]

		labels = {
			'cod_responsable':'Código',
			'dui':'DUI',
			'nit':'NIT',
			'nombres':'Nombre(s)',
			'apellidos':'Apellido(s)',
			'direccion':'Direccion',
		}

		widgets = {
			'cod_responsable':forms.TextInput(attrs={'class':'form-control'}),
			'dui':forms.TextInput(attrs={'class':'form-control'}),
			'nit':forms.TextInput(attrs={'class':'form-control'}),
			'nombres':forms.TextInput(attrs={'class':'form-control'}),
			'apellidos':forms.TextInput(attrs={'class':'form-control'}),
			'direccion':forms.TextInput(attrs={'class':'form-control'}),
		}

#Formulario para registrar nueva unidad de Transporte
class UnidadForm(forms.ModelForm):
	class Meta:
		model = UnidadTransporte

		fields = [
			'cod_unidad',
			'ruta',
			'placa',
			'motorista',
		]

		labels = {
			'cod_unidad':'Unidad',
			'ruta':'Ruta',
			'placa':'Placa',
			'motorista':'Nombre (Mote)',
		}

		widgets = {
			'cod_unidad':forms.TextInput(attrs={'class':'form-control'}),
			'ruta':forms.TextInput(attrs={'class':'form-control'}),
			'placa':forms.TextInput(attrs={'class':'form-control'}),
			'motorista':forms.Select(attrs={'class':'form-control'}),
		}
		
#Formulario para crear puntos de control
class FormularioPuntos(forms.ModelForm):
	class Meta:
		model = PuntoControl

		fields = [
			'cod_punto',
			'ubicacion',
			'responsable',
		]

		labels = {
			'cod_punto':'Código del Punto',
			'ubicacion':'Ubicacion del punto',
			'responsable':'Responsable del punto',
		}

		widgets = {
			'cod_punto':forms.TextInput(attrs={'class':'form-control'}),
			'ubicacion':forms.TextInput(attrs={'class':'form-control'}),
			'responsable':forms.Select(attrs={'class':'form-control'}),
			}

#Formulario que permite cambiar el motorista de una unidad
class CambioMotoristaForm(forms.ModelForm):
	class Meta:
		model = UnidadTransporte

		fields = [
			'motorista',
		]

		labels = {
			'motorista':'Motoristas',
		}

		widgets = {
			'motorista':forms.Select(attrs={'class':'form-control'}),
		}

