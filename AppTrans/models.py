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
	cod_unidad = models.CharField(max_length=10)
	ruta = models.IntegerField(null=False, default=0)
	placa = models.CharField(max_length=15)
	nombre_mote = models.CharField(max_length=20, default='No tiene nombre')
	motorista = models.OneToOneField(Motorista, on_delete=models.CASCADE, default='No Asignado', null=True, blank=True)

	def __str__(self):
		return '%s %s' % (self.nombre_mote, self.placa)

class PuntoControl(models.Model):
	cod_punto = models.CharField(max_length=10)
	ubicacion = models.CharField(max_length=60)
	responsable = models.OneToOneField(ResponsablePunto, on_delete=models.CASCADE)  

	def __str__(self):
		return '%s %s' % (self.id, self.cod_punto)

class RegistroLlegada(models.Model):
	cod_registro = models.CharField(max_length=10)
	punto = models.ForeignKey(PuntoControl, on_delete=models.CASCADE, default=1)
	unidad = models.ForeignKey(UnidadTransporte, on_delete=models.CASCADE, default=1)
	responsable = models.ForeignKey(ResponsablePunto, on_delete=models.CASCADE, default=1)
	fecha = models.DateField(auto_now_add=True)
	hora = models.TimeField(auto_now_add=True)
	num_pasajeros = models.IntegerField(null=True, blank=True, default=0)
	cant_dinero = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)

	def __str__(self):
		return '%s %s %s' % (self.cod_registro, self.responsable.cod_responsable, self.fecha)