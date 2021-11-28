
from django.urls.conf import path
from .views import inicio, lista_clientes, lista_autos, lista_viajes, crear_viajes, crear_autos, crear_clientes


urlpatterns = [
    path('', inicio, name='Inicio'),
    path('clientes/', lista_clientes, name='Clientes'),
    path('clientes/crear/', crear_clientes, name='Crear_cliente'),
    path('autos/', lista_autos, name='Autos'),
    path('autos/crear/', crear_autos, name='Crear_auto'),
    path('viajes/', lista_viajes, name='Viajes'),
    path('viajes/crear/', crear_viajes, name='Crear_viaje'),
]