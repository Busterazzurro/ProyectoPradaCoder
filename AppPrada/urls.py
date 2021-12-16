
from django.urls.conf import path
from django.urls.resolvers import URLPattern
from .views import EmpresasDetailView, about, empresas_view, index, login_request, register_request, editar_user, empresas_view, comentarios_view, clientes_view, editar_avatar
from django.contrib.auth.views import LogoutView
from django import template
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', index, name='Index'),
    
    path('login/', login_request, name='Login'),
    path('logout/', LogoutView.as_view(template_name='AppPrada/logout.html'), name='Logout'),
    path('registro/', register_request, name='Register'),
    path('editar/', editar_user, name='Editar'),
    path('editaravatar/', editar_avatar, name='Editar_avatar'),
    
    path('about/', about, name='About'),
    
    path('empresas/', empresas_view, name='empresas'),
    path('empresas/agregar/', views.agregarempresa, name='agregarempresas'),
    path('empresas/eliminar/<int:empresas_id>/', views.eliminarempresa, name='eliminarempresas'),
    path('empresas/editar/<int:empresas_id>/', views.editarempresa, name='editarempresas'),
    path('empresas/<int:pk>/', EmpresasDetailView.as_view(), name='detalle_empresa'),
    
    path('clientes/', clientes_view, name='clientes'),
    path('clientes/agregar/', views.agregarcliente, name='agregarclientes'),
    path('clientes/eliminar/<int:clientes_id>/', views.eliminarcliente, name='eliminarclientes'),
    path('clientes/editar/<int:clientes_id>/', views.editarcliente, name='editarclientes'),
    
    path('comentarios/', comentarios_view, name='comentarios'),
    path('comentarios/agregar/', views.agregarcomentario, name='agregarcomentarios'),
    path('comentarios/eliminar/<int:comentarios_id>/', views.eliminarcomentario, name='eliminarcomentarios'),
    path('comentarios/editar/<int:comentarios_id>/', views.editarcomentario, name='editarcomentarios'),
]