from django.http import HttpResponse
from django.shortcuts import render
from clase.models import Curso
from clase.forms import CursoFormulario, BusquedaCurso
import random    

# Create your views here.

def nuevo_curso(request):
    camada = random.randrange(1500, 3000)
    nuevo_curso = Curso(nombre='Curso Pyhon', camada=camada)
    nuevo_curso.save()
    return HttpResponse(f"Se creo el curso {nuevo_curso.nombre} camada {nuevo_curso.camada}")

def formulario_curso(request):
    
    # Sin formularios de django
    # print(request.method)
    # if request.method == 'POST':
    #     print(request.POST)
    #     nuevo_curso = Curso(nombre=request.POST['curso'], camada=request.POST['camada'])
    #     nuevo_curso.save()
    #     return render(request, 'indice/index.html', {'nuevo_curso': nuevo_curso})
        
    # return render(request, 'clase/formulario_curso.html', {})
    
    # Con formularios de django
    if request.method == 'POST':
        formulario = CursoFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_curso = Curso(nombre=data['curso'], camada=data['camada'])
            nuevo_curso.save()
            return render(request, 'indice/index.html', {'nuevo_curso': nuevo_curso})
            
    formulario = CursoFormulario()
    return render(request, 'clase/formulario_curso.html', {'formulario': formulario})

def busqueda_curso(request):
    cursos_buscados = []
    dato = request.GET.get('partial_curso', None)
    
    if dato is not None:
        # cursos_buscados = Curso.objects.get(nombre=dato)
        # cursos_buscados = Curso.objects.filter(nombre=dato)
        cursos_buscados = Curso.objects.filter(nombre__icontains=dato)
    
    buscador = BusquedaCurso()
    return render(
        request, "clase/busqueda_curso.html",
        {'buscador': buscador, 'cursos_buscados': cursos_buscados, 'dato': dato}
    )