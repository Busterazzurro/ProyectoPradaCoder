from django.contrib import admin

from .models import Avatar, Clientes, Empresas, Comentarios
# Register your models here.


#Nuevos

admin.site.register(Clientes)
admin.site.register(Empresas)
admin.site.register(Comentarios)
admin.site.register(Avatar)