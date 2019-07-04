from django.contrib import admin
from AppTrans.models import Motorista, ResponsablePunto, UnidadTransporte, RegistroLlegada, PuntoControl

# Register your models here.

admin.site.register(Motorista)
admin.site.register(ResponsablePunto)
admin.site.register(UnidadTransporte)
admin.site.register(RegistroLlegada)
admin.site.register(PuntoControl)