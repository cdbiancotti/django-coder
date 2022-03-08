from django.http import HttpResponse
import random
from django.shortcuts import render

from django.template import loader


def inicio(request):
    return render(request, "indice/index.html", {})

def otro_vista(request):
    return HttpResponse('''
                        <h1>Este es un titulo en h1</h1>
                        ''')
    
def numero_random(request):
    numero = random.randrange(15, 180)
    texto = f'<h1>Este es tu numero random: {numero}</h1>'
    return HttpResponse(texto)

def numero_del_usuario(request, numero):
    texto = f'<h1>Este es tu numero: {numero}</h1>'
    return HttpResponse(texto)

def mi_plantilla(request):
    
    nombre = 'Jorgelina'
    apellido = 'Atahualpa'
    lista = [3,1,2,45,1,2,3]
    
    diccionario_de_datos = {
        'nombre': nombre,
        'apellido': apellido,
        'nombre_largo': len(nombre),
        'lista': lista
    }
    
    #version vieja con open
    # plantilla = open(r"C:\Users\quiti\Desktop\miproyecto\miproyecto\plantillas\mi_plantilla.html")
    # template = Template(plantilla.read())
    # plantilla.close()
    # context = Context(diccionario_de_datos)
    # plantilla_preparada = template.render(diccionario_de_datos)

    # version nueva con loader
    # template = loader.get_template("mi_plantilla.html")
    # plantilla_preparada = template.render(diccionario_de_datos)
    # return HttpResponse(plantilla_preparada)
    
    # version con render
    return render(request, "indice/mi_plantilla.html", diccionario_de_datos)
    