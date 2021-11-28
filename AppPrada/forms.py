

from django import forms

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