from django import forms

from transporte.models import RegistroLlegada

class FormRegistroLlegada(forms.ModelForm):
	class Meta:
		model = RegistroLlegada
		
		fields=[
			'cod_registro',
			'unidad',
			'responsable',
			'fecha',
			'hora',
			'num_pasajeros',
		]

		labels={
			'cod_responsable':'Código',
			'unidad':'Unidad de Transporte',
			'responsable':'Autor de Registro',
			'fecha':'Fecha',
			'hora':'Hora',
			'num_pasajeros':'Cantidad de pasajeros',
		}

		widgets={
			'cod_responsable':forms.TextInput(attrs={'class':'form-control'}),
			'unidad':forms.Select(attrs={'class':'form-control'}),
			'responsable':forms.Select(attrs={'class':'form-control'}),
			'fecha':forms.TextInput(attrs={'class':'form-control'}),
			'hora':forms.TextInput(attrs={'class':'form-control'}),
			'num_pasajeros':forms.TextInput(attrs={'class':'form-control'}),
		}