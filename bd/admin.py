from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Ciclo)
admin.site.register(Curso)
admin.site.register(Grupo)
admin.site.register(Modulo)
admin.site.register(Profesor)
admin.site.register(Reparto)
admin.site.register(ModulosAsignados)
admin.site.register(ModulosNoAsignados)