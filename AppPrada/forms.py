

from django import forms
from .models import Empresas, Clientes, Comentarios

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
    
#class RegistroUser(UserCreationForm):
#    email = forms.EmailField(label='Email')
#    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
#    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
#    class Meta:
 #       model = User
#        fields = ['username', 'password1', 'password2', 'email']
#        help_texts = {k: '' for k in fields}


class EditarUsuarioForm(UserCreationForm):
    username = forms.CharField(label='Username')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','password1', 'password2']
        help_texts = {k: '' for k in fields}



class EmpresasForm(forms.ModelForm):
    class Meta:
        model = Empresas
        fields = ['nombre_empresa', 'email_empresa', 'tamano_camion', 'imagen']
        
class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nombre', 'apellido','email', 'barrio', 'destino']
        
class ComentariosForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ['nombre_empresa', 'puntuacion', 'comentario']
        
class AvatarForm(forms.Form):
    avatar = forms.ImageField()