from django.db import models

# Create your models here.

class Motorista(models.Model):
	cod_motorista = models.CharField(max_length=10)
	dui = models.CharField(max_length=15)
	nit = models.CharField(max_length=20)
	nombres = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=30)
	direccion = models.CharField(max_length=60)

	def __str__(self):
		return '%s %s' % (self.nombres, self.apellidos)

class ResponsablePunto(models.Model):
	cod_responsable = models.CharField(max_length=10)
	dui = models.CharField(max_length=15)
	nit = models.CharField(max_length=20)
	nombres = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=30)
	direccion = models.CharField(max_length=60)

	def __str__(self):
		return '%s %s' % (self.nombres, self.apellidos)

class UnidadTransporte(models.Model):
	cod_unidad = models.CharField(max_length=10,default=False)
	placa = models.CharField(max_length=15, default=False)
	nombre_mote = models.CharField(max_length=20, default=False)
	motorista = models.OneToOneField(Motorista, on_delete=False, default=False)

	def __str__(self):
		return '%s %s' % (self.motorista.cod_motorista, self.placa)

class PuntoControl(models.Model):
	cod_punto = models.CharField(max_length=10)
	nombre_punto = models.CharField(max_length=25)
	ubicacion = models.CharField(max_length=60)
	responsable = models.OneToOneField(ResponsablePunto, on_delete=False)  

	def __str__(self):
		return '%s %s %s' % (self.cod_punto, self.nombre_punto, self.responsable.cod_responsable)

class RegistroLlegada(models.Model):
	cod_registro = models.CharField(max_length=10, default=False)
	unidad = models.ForeignKey(UnidadTransporte, null=False, on_delete=models.CASCADE, default=False)
	responsable = models.ForeignKey(ResponsablePunto, null=False, on_delete=models.CASCADE, default=False)
	fecha = models.DateField()
	hora = models.TimeField()
	num_pasajeros = models.IntegerField(null=True, blank=True, default=False)

	def __str__(self):
		return '%s %s %s' % (self.cod_registro, self.responsable.cod_responsable, self.fecha)