
from django.urls.conf import path
from .views import about, index, inicio, lista_clientes, lista_autos, lista_viajes, crear_viajes, crear_autos, crear_clientes, login_request, register_request
from django.contrib.auth.views import LogoutView
from django import template


urlpatterns = [
    path('', inicio, name='Inicio'),
    path('clientes/', lista_clientes, name='Clientes'),
    path('clientes/crear/', crear_clientes, name='Crear_cliente'),
    path('autos/', lista_autos, name='Autos'),
    path('autos/crear/', crear_autos, name='Crear_auto'),
    path('viajes/', lista_viajes, name='Viajes'),
    path('viajes/crear/', crear_viajes, name='Crear_viaje'),
    path('login/', login_request, name='Login'),
    path('logout/', LogoutView.as_view(template_name='AppPrada/logout.html'), name='Logout'),
    path('registro/', register_request, name='Register'),  
    
    path('index/', index, name='Index'),
    
    path('about/', about, name='About'),
]