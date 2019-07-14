from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Motorista(models.Model):
	cod_motorista = models.CharField(max_length=10)
	dui = models.CharField(max_length=15)
	nit = models.CharField(max_length=20)
	nombres = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=30)
	direccion = models.CharField(max_length=40,null=True)

	def __str__(self):
		return '%s %s' % (self.nombres, self.apellidos)

	def obtener_cod(self):
		return 'M-'+ str(self.pk).zfill(5)

class ResponsablePunto(models.Model):
	cod_responsable = models.CharField(max_length=10)
	dui = models.CharField(max_length=15)
	nit = models.CharField(max_length=20)
	nombres = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=30)
	direccion = models.CharField(max_length=40,null=True)

	def __str__(self):
		return '%s %s' % (self.nombres, self.apellidos)

	def obtener_cod(self):
		return 'R-'+ str(self.pk).zfill(5)

class UnidadTransporte(models.Model):
	cod_unidad = models.CharField(max_length=10)
	ruta = models.CharField(max_length=5, null=False, default=0)
	placa = models.CharField(max_length=15)
	nombre_mote = models.CharField(max_length=20, default='No tiene nombre')
	motorista = models.OneToOneField(Motorista, on_delete=models.CASCADE, default=1, null=True, blank=True)


	def __str__(self):
		return '%s %s' % (self.nombre_mote, self.placa)

	def obtener_cod(self):
		return 'U-'+ str(self.pk).zfill(5)

class PuntoControl(models.Model):
	cod_punto = models.CharField(max_length=10)
	ubicacion = models.CharField(max_length=60)
	responsable = models.OneToOneField(ResponsablePunto, on_delete=models.CASCADE, null=True, blank=True)  

	def __str__(self):
		return '%s' % (self.cod_punto)

	def obtener_cod(self):
		return 'P-'+ str(self.pk).zfill(5)

class RegistroLlegada(models.Model):
	cod_registro = models.CharField(max_length=10, default='R-00000')
	punto = models.ForeignKey(PuntoControl, on_delete=models.CASCADE, default=1)
	unidad = models.ForeignKey(UnidadTransporte, on_delete=models.CASCADE, default=1)
	responsable = models.ForeignKey(ResponsablePunto, on_delete=models.CASCADE, default=1)
	fecha = models.DateField(auto_now_add=True)
	hora = models.TimeField(auto_now_add=True)
	num_pasajeros = models.IntegerField(null=True, blank=True, default=0)
	cant_dinero = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)

	def __str__(self):
		return '%s %s %s' % (self.cod_registro, self.responsable.cod_responsable, self.fecha)

	def obtener_cod(self):
		return 'R-'+ str(self.pk).zfill(5)	