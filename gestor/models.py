from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Usuario(models.Model):
    nombre = models.TextField(max_length=100)
    email = models.TextField(max_length=200, unique=True)
    contraseña = models.TextField(max_length=100)
    fecharegistro = models.DateTimeField(default=timezone.now)

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    prioridad = models.IntegerField(max_length=20)
    estado = models.Choices('Pendiente','Progreso','Completada')
    completada = models.BooleanField()
    fechacreacion = models.DateTimeField(default=timezone.now)
    horavencimiento = models.TimeField()
    
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    duracionestimada = models.FloatField(max_length=20)
    fechainicio = models.DateTimeField(default=timezone.now)
    fechafinalizacion = models.DateTimeField()

class Etiqueta (models.Model):
    nombre = models.CharField(max_length=100, unique=True)

class AsignacionTarea(models.Model):
    observaciones = models.TextField(max_length=200)
    fechadeasignacion = models.DateField(default=timezone.now)
# Etiqueta:

# Nombre: Texto y único

# Asignación de Tarea:

# Observaciones: Texto largo
# Fecha de Asignación : Fecha y Hora

# Comentario:

# Contenido: Texto Largo
# Fecha de Comentario: Fecha y Hora
