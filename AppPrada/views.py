from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Cliente, Auto, Viaje
from .forms import ClientesFormulario, AutosFormulario, ViajesFormulario

#INICIO
def inicio(request):
    
    return render(request, 'AppPrada/Inicio.html', {})

#CLIENTES
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

#AUTOS
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
