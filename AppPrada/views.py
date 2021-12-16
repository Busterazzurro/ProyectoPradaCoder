from django import template
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import  Avatar, Clientes, Comentarios, Empresas
from .forms import AvatarForm, EditarUsuarioForm, EmpresasForm, ClientesForm, ComentariosForm
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView


#INICIO
def inicio(request):
    
    return render(request, 'AppPrada/Inicio.html', {})



#INDEX

def about(request):
    
    return render(request, 'AppPrada/about.html', {}) 

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
                return render(request, 'AppPrada/index.html', {'tiene_mensaje': True, 'mensaje': f"Te logueaste con exito {username}!"})
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
            
            return render(request, 'AppPrada/index.html', {'tiene_mensaje': True, 'mensaje': f'Se Registró el user: {username}!'})
           
    form = UserCreationForm()
    
    return render(request, 'AppPrada/register.html', {'form': form, 'mensaje': '','error': False})

#########################################################################
#EDITAR_USER

@login_required
def editar_user(request):
    
    username = request.user
    
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST)
        
        if form.is_valid():
            
            datos = form.cleaned_data
            
            username.username = datos['username']
            username.password1 = datos['password1']
            username.password2 = datos['password2']
            username.first_name = datos['first_name']
            username.last_name = datos['last_name']
            
            username.save()
            
            return render(request, 'AppPrada/index.html', {'tiene_mensaje': True, 'mensaje':'Se Editó Correctamente!'})
    else:
               
        form = EditarUsuarioForm(initial={'username': username.username})
    
    return render(request, 'AppPrada/editar_user.html', {'form': form})


############################################
#nuevos

#INDEX

def index(request):

    return render(request, 'AppPrada/index.html', {}) 

#empresas
def empresas_view(request):
    empresa = Empresas.objects.all()
    context= {'empresas':empresa}
    return render(request, 'AppPrada/empresas.html', context) 

@login_required
def agregarempresa(request):
    if request.method == "POST":
        form = EmpresasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('empresas')
    else:
        form = EmpresasForm()
    
    context = {'form': form}
    return  render(request, 'AppPrada/agregarempresa.html', context )


@login_required
def eliminarempresa(request, empresas_id):
    empresas = Empresas.objects.get(id=empresas_id)
    empresas.delete()
    return redirect("empresas")

@login_required
def editarempresa(request, empresas_id,):
    empresas = Empresas.objects.get(id=empresas_id)
    if request.method == "POST":
        form = EmpresasForm(request.POST,request.FILES, instance=empresas)
        if form.is_valid():
            form.save()
            return redirect("empresas")
    else:
        form = EmpresasForm(instance=empresas)
    context = {'form': form}
    return render(request, 'AppPrada/editarempresa.html', context)

#clientes
def clientes_view(request):
    cliente = Clientes.objects.all()
    context= {'clientes':cliente}
    return render(request, 'AppPrada/clientes.html', context) 

@login_required
def agregarcliente(request):
    if request.method == "POST":
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClientesForm()
    
    context = {'form': form}
    return  render(request, 'AppPrada/agregarcliente.html', context )

@login_required
def eliminarcliente(request, clientes_id):
    clientes = Clientes.objects.get(id=clientes_id)
    clientes.delete()
    return redirect("clientes")

@login_required
def editarcliente(request, clientes_id):
    clientes = Clientes.objects.get(id=clientes_id)
    if request.method == "POST":
        form = ClientesForm(request.POST, instance=clientes)
        if form.is_valid():
            form.save()
            return redirect("clientes")
    else:
        form = ClientesForm(instance=clientes)
    context = {'form': form}
    return render(request, 'AppPrada/editarcliente.html', context)
    
#comentarios
def comentarios_view(request):
    comentario = Comentarios.objects.all()
    context= {'comentarios':comentario}
    return render(request, 'AppPrada/comentarios.html', context) 

@login_required
def agregarcomentario(request):
    if request.method == "POST":
        form = ComentariosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comentarios')
    else:
        form = ComentariosForm()
    
    context = {'form': form}
    return  render(request, 'AppPrada/agregarcomentario.html', context )

@login_required
def eliminarcomentario(request, comentarios_id):
    comentarios = Comentarios.objects.get(id=comentarios_id)
    comentarios.delete()
    return redirect("comentarios")

@login_required
def editarcomentario(request, comentarios_id):
    comentarios = Comentarios.objects.get(id=comentarios_id)
    if request.method == "POST":
        form = ComentariosForm(request.POST, instance=comentarios)
        if form.is_valid():
            form.save()
            return redirect("comentarios")
    else:
        form = ComentariosForm(instance=comentarios)
    context = {'form': form}
    return render(request, 'AppPrada/editarcomentario.html', context)

class EmpresasDetailView(DetailView):
    model = Empresas
    template_name = "AppPrada/detalle_empresa.html"

#avatar de usuario
@login_required
def editar_avatar(request):
    
    username = request.user
    
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            avatar = Avatar(user=username, avatar=form.cleaned_data['avatar'])
            
            avatar.save()
            
            return render(request, 'AppPrada/index.html', 
                          {'tiene_mensaje': True, 'mensaje':'Se Cargó Correctamente el Avatar!', 'url_avatar': avatar.avatar.url})
    else:
               
        form = AvatarForm()
    
    return render(request, 'AppPrada/editar_avatar.html', {'form': form})