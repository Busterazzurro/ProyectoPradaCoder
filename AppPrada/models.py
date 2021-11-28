from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    numero=models.IntegerField()

    def __str__(self):
        return f'Cliente Numero: {self.numero}. Nombre: {self.nombre}. Apellido: {self.apellido}'
class Auto(models.Model):
    modelo=models.CharField(max_length=20)
    marca=models.CharField(max_length=20)
    id_auto=models.IntegerField()

    def __str__(self):
        return f'ID de auto  {self.id_auto}. Modelo: {self.modelo}. Marca: {self.marca}'
    
class Viaje(models.Model):
    origen=models.CharField(max_length=20)
    destino=models.CharField(max_length=20)
    conductor=models.CharField(max_length=20)
    preferencia_aire_acondicionado=models.BooleanField()
    pago_online=models.BooleanField()
    id_viaje=models.IntegerField()
    
    def __str__(self):
        return f'ID de viaje: {self.id_viaje}. Origen: {self.origen}. Destino: {self.destino}'