from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    #nuevas clasess
class Clientes(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    email=models.EmailField()
    barrio=models.CharField(max_length=20)
    destino=models.CharField(max_length=20)
    
    def __str__(self):
        return f' Nombre: {self.nombre}. Apellido: {self.apellido}. Email: {self.email}. Barrio: {self.barrio}. Destino: {self.destino}.'
class Empresas(models.Model):
    nombre_empresa=models.CharField(max_length=20)
    email_empresa=models.EmailField()
    tamano_camion=models.CharField(max_length=20)
    imagen=models.ImageField(upload_to='empresas', null=True, blank=True)
    
    def __str__(self):
        return f' Nombre de la Empresa: {self.nombre_empresa}. Email: {self.email_empresa}. Tamaño del Camion: {self.tamano_camion}.'
        
class Comentarios(models.Model):
    nombre_empresa=models.CharField(max_length=20)
    puntuacion=models.CharField(max_length=1)
    comentario=models.CharField(max_length=50)
    
    def __str__(self):
        return f' Nombre de la Empresa: {self.nombre_empresa}. Puntuacion (0-5): {self.puntuacion}. Comentario: {self.comentario}.'
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=False, blank=False)