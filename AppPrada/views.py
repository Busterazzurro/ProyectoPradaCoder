from django import template
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Cliente, Auto, Viaje
from .forms import ClientesFormulario, AutosFormulario, ViajesFormulario
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

#INICIO
def inicio(request):
    
    return render(request, 'AppPrada/Inicio.html', {})

#INDEX

def index(request):
    
    return render(request, 'AppPrada/index.html', {}) 

#INDEX

def about(request):
    
    return render(request, 'AppPrada/about.html', {}) 

######################################################
#CLIENTES
@login_required
def lista_clientes(request):
    clientes = None
    error = None
    if request.method == 'GET':
        numero = request.GET.get('numero', '')
        if numero =='':
            clientes = Cliente.objects.all()
        else:
            try:
                numero = int(numero)
                clientes = Cliente.objects.filter(numero=numero)
            except:
                error = 'Debes ingresar un numero entero'

    return render(request, 'AppPrada/lista_clientes.html', {'clientes': clientes, 'error': error})

#Crear Cliente
@login_required
def crear_clientes(request):
    
    if request.method == 'POST':
        formulario = ClientesFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            cliente = Cliente(nombre=datos['nombre'],apellido=datos['apellido'],numero=datos['numero'])
            cliente.save()
            #return render(request, 'AppPrada/lista_clientes.html', {'clientes': None, 'error': None})
            return redirect('Clientes')
    
    formulario = ClientesFormulario()
    return render(request, 'AppPrada/formulario_cliente.html', {'formulario': formulario})

#######################################################################################
#AUTOS
@login_required
def lista_autos(request):
    autos = None
    error = None
    if request.method == 'GET':
        id_auto = request.GET.get('id_auto', '')
        if id_auto =='':
            autos = Auto.objects.all()
        else:
            try:
                id_auto = int(id_auto)
                autos = Auto.objects.filter(id_auto=id_auto)
            except:
                error = 'Debes ingresar un numero entero'
                
    return render(request, 'AppPrada/lista_autos.html', {'autos': autos, 'error': error})

#Crear Auto
@login_required
def crear_autos(request):
    
    if request.method == 'POST':
        formulario = AutosFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            auto = Auto(modelo=datos['modelo'],marca=datos['marca'],id_auto=datos['id_auto'])
            auto.save()
            #return render(request, 'AppPrada/lista_autos.html', {'autos': None, 'error': None})
            return redirect('Autos')
    
    formulario = AutosFormulario()
    return render(request, 'AppPrada/formulario_auto.html', {'formulario': formulario})

#VIAJES
@login_required
def lista_viajes(request):
    viajes = None
    error = None
    if request.method == 'GET':
        id_viaje = request.GET.get('id_viaje', '')
        if id_viaje =='':
            id_viaje = Viaje.objects.all()
        else:
            try:
                id_viaje = int(id_viaje)
                viajes = Viaje.objects.filter(id_viaje=id_viaje)
            except:
                error = 'Debes ingresar un numero entero'

    return render(request, 'AppPrada/lista_viajes.html', {'viajes': viajes, 'error': error})

#Crear Viaje
@login_required
def crear_viajes(request):
    
    if request.method == 'POST':
        formulario = ViajesFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            viaje = Viaje(origen=datos['origen'],destino=datos['destino'],conductor=datos['conductor'],preferencia_aire_acondicionado=datos['preferencia_aire_acondicionado'],pago_online=datos['pago_online'],id_viaje=datos['id_viaje'])
            viaje.save()
            #return render(request, 'AppPrada/lista_viajes.html', {'autos': None, 'error': None})
            return redirect('Viajes')
    
    formulario = ViajesFormulario()
    return render(request, 'AppPrada/formulario_viaje.html', {'formulario': formulario})

######################################################

#LOGIN

def login_request(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return render(request, 'AppPrada/inicio.html', {'tiene_mensaje': True, 'mensaje': f"Te logueaste con exito {username}!"})
            else:
                return render(request, 'AppPrada/login.html', {'form': form,'mensaje': "Error! User/Password Incorrecto", 'error': True})
            
        else:
            return render(request, 'AppPrada/login.html', {'form': form,'mensaje': "Error! User/Password Incorrecto", 'error': True})
            
    
    form = AuthenticationForm
    
    return render(request, 'AppPrada/login.html', {'form': form, 'mensaje': '','error': False})

#########################################################################
#REGISTRO

def register_request(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            
            form.save()
            
            return render(request, 'AppPrada/inicio.html', {'tiene_mensaje': True, 'mensaje': f'Se Registró el user: {username}!'})
           
    form = UserCreationForm()
    
    return render(request, 'AppPrada/register.html', {'form': form, 'mensaje': '','error': False})

