

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
class ClientesFormulario(forms.Form):
    nombre=forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=20)
    numero=forms.IntegerField()
    
class AutosFormulario(forms.Form):
    modelo=forms.CharField(max_length=20)
    marca=forms.CharField(max_length=20)
    id_auto=forms.IntegerField()
    
class ViajesFormulario(forms.Form):
    origen=forms.CharField(max_length=20)
    destino=forms.CharField(max_length=20)
    conductor=forms.CharField(max_length=20)
    preferencia_aire_acondicionado=forms.BooleanField()
    pago_online=forms.BooleanField()
    id_viaje=forms.IntegerField()
    
#class RegistroUser(UserCreationForm):
#    email = forms.EmailField(label='Email')
#    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
#    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
#    class Meta:
 #       model = User
#        fields = ['username', 'password1', 'password2', 'email']
#        help_texts = {k: '' for k in fields}
        