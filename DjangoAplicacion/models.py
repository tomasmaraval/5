from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Curso (models.Model):
    curso = models.CharField(max_length=40, null=False)
    camada = models.IntegerField(null=False)

    def __str__(self) -> str:
        return f'Curso: {self.curso}, Camada: {self.camada}'

class Profesor (models.Model):
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    email = models.EmailField(null=False)
    profesion = models.CharField(max_length=30, null=False)

    def __str__(self) -> str:
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}, Profesion: {self.profesion}'

class Estudiante (models.Model):
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    email = models.EmailField(null=False)

    def __str__(self) -> str:
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}'

class Entregable (models.Model):
    nombre = models.CharField(max_length=30, null=False)
    fecha_entrega = models.DateField(null=False)
    entregado = models.BooleanField(null=False)

    def __str__(self) -> str:
        return f'Nombre: {self.nombre}, Fecha de entrega: {self.fecha_entrega}, Entregado: {self.entregado}'
    
class Avatar (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self) -> str:
        return f'Avatar de: {self.user}'