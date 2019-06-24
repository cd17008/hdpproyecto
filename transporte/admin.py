from django.contrib import admin
from transporte.models import Motorista, ResponsablePunto, UnidadTransporte, RegistroLlegada

# Register your models here.

admin.site.register(Motorista)
admin.site.register(ResponsablePunto)
admin.site.register(UnidadTransporte)
admin.site.register(RegistroLlegada)