from django import forms
from AppTrans.models import RegistroLlegada

class FormularioRegistro(forms.ModelForm):
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

class FormularioUnidades(forms.ModelForm):
	class Meta:
		model = RegistroLlegada

		fields = [
			'unidad',
		]

		labels = {
			'unidad':'Unidades'
		}

		widgets = {
			'unidad':forms.RadioSelect(),
		}