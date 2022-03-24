from django.http import HttpResponse
import random
from django.shortcuts import render, redirect

from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import NuestraCreacionUser, NuestraEdicionUser
from django.contrib.auth.decorators import login_required
from .models import Avatar

# from django.template import loader

def inicio(request):
    return render(request, "indice/index.html", {'user_avatar_url': buscar_url_avatar(request.user)})

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
    
def login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                django_login(request, user)
                return render(request, 'indice/index.html', {'msj': 'Te logueaste!'})
            else:
                return render(request, 'indice/login.html', {'form': form, 'msj': 'No se autentico'})
            
        else:
            return render(request, 'indice/login.html', {'form': form, 'msj': 'datos con formato incorrecto'})
    else:
        form = AuthenticationForm()
        return render(request, 'indice/login.html', {'form': form, 'msj': ''})
    
def registrar(request):
    
    if request.method == 'POST':
        form = NuestraCreacionUser(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'indice/index.html', {'msj': f'Se creo el user {username}'})
        else:
            return render(request, 'indice/registrar.html', {'form': form, 'msj': ''})
    
    form = NuestraCreacionUser()
    return render(request, 'indice/registrar.html', {'form': form, 'msj': ''})

@login_required
def editar(request):
    msj = ''
    if request.method == 'POST':
        form = NuestraEdicionUser(request.POST)
        
        if form.is_valid():
            
            data = form.cleaned_data
            
            # request.user.email = data.get('email')
            # request.user.first_name = data.get('first_name', '')
            # request.user.last_name = data.get('last_name', '')
            # request.user.password1 = data.get('password1')
            # request.user.password2 = data.get('password2')
            
            # request.user.save()
            
            
            logued_user = request.user
            logued_user.email = data.get('email')
            logued_user.first_name = data.get('first_name', '')
            logued_user.last_name = data.get('last_name', '')
            if data.get('password1') == data.get('password2') and len(data.get('password1')) > 8:
                logued_user.set_password(data.get('password1'))
            else:
                msj = 'No se modifico el password.'
            
            logued_user.save()
            
            return render(request, 'indice/index.html', {'msj': msj, 'user_avatar_url': buscar_url_avatar(request.user)})
        else:
            return render(request, 'indice/editar_user.html', {'form': form, 'msj': '', 'user_avatar_url': buscar_url_avatar(request.user)})
    
    form = NuestraEdicionUser(
        initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'username': request.user.username
        }
    )
    return render(request, 'indice/editar_user.html', {'form': form, 'msj': '', 'user_avatar_url': buscar_url_avatar(request.user)})


def buscar_url_avatar(user):
    return Avatar.objects.filter(user=user)[0].imagen.url