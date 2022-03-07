from django.http import HttpResponse
from django.shortcuts import render
from clase.models import Curso
import random    

# Create your views here.

def nuevo_curso(request):
    camada = random.randrange(1500, 3000)
    nuevo_curso = Curso(nombre='Curso Pyhon', camada=camada)
    nuevo_curso.save()
    5-5
    return HttpResponse(f"COSA RARA AGREGADA - Se creo el curso {nuevo_curso.nombre} camada {nuevo_curso.camada}")
