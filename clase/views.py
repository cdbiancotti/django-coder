from django.http import HttpResponse
from django.shortcuts import render, redirect
from clase.models import Curso, Estudiante, Profesor
from clase.forms import CursoFormulario, BusquedaCurso, EstudianteFormulario
import random
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView

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
    

# CRUD Basico

def listado_estudiantes(request):
    listado_estudiantes = Estudiante.objects.all()
    return render(
        request, "clase/listado_estudiantes.html",
        {'listado_estudiantes': listado_estudiantes}
    )
    
def crear_estudiante(request):
    if request.method == 'POST':
        formulario = EstudianteFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_estudiante = Estudiante(
                nombre=data['nombre'], 
                apellido=data['apellido'],
                email=data['email']
            )
            nuevo_estudiante.save()
            return redirect('listado_estudiantes')
            
            
    formulario = EstudianteFormulario()
    return render(
        request, 'clase/crear_estudiante.html', 
        {'formulario': formulario}
    )

def actualizar_estudiante(request, id):
    
    estudiante = Estudiante.objects.get(id=id)
    
    if request.method == 'POST':
        formulario = EstudianteFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            estudiante.nombre = data['nombre']
            estudiante.apellido = data['apellido']
            estudiante.email = data['email']
            estudiante.save()
            return redirect('listado_estudiantes')
            
    formulario = EstudianteFormulario(
        initial={
            'nombre': estudiante.nombre,
            'apellido': estudiante.apellido,
            'email': estudiante.email
        }
    )
    return render(
        request, 'clase/actualizar_estudiante.html', 
        {'formulario': formulario, 'estudiante': estudiante}
    )
    
def borrar_estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    estudiante.delete()
    return redirect('listado_estudiantes')

# CRUD con CBV

# class Profesor(models.Model):
#     nombre = models.CharField(max_length=20)
#     apellido = models.CharField(max_length=30)
#     email = models.EmailField()
#     profesión = models.CharField(max_length=30)


class ProfesorLista(ListView):
    model = Profesor
    template_name = '/clase/profesor_list.html'


class ProfesorDetalle(DetailView):
    model = Profesor
    template_name = '/clase/profesor_datos.html'


class ProfesorEditar(UpdateView):
    model = Profesor
    success_url = '/clase/profesor_list.html'
    fields = ['nombre', 'apellido', 'email', 'profesión']


class ProfesorBorrar(DeleteView):
    model = Profesor
    success_url = 'clase/profesor_listado'