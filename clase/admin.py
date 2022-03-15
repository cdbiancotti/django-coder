from django.contrib import admin

from .models import Curso, Profesor, Entregable, Estudiante

# Register your models here.

admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Entregable)
admin.site.register(Estudiante)