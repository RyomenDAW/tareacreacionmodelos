from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Usuario(models.Model):
    nombre = models.TextField(max_length=100)
    email = models.TextField(max_length=200, unique=True)
    contraseña = models.TextField(max_length=100)
    fecharegistro = models.DateTimeField(default=timezone.now)

    
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    duracionestimada = models.FloatField(max_length=20)
    fechainicio = models.DateTimeField(default=timezone.now)
    fechafinalizacion = models.DateTimeField()
    
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='proyectos_creados')

    colaboradores = models.ManyToManyField(Usuario, related_name='proyectos_asignados')


class Etiqueta (models.Model):
    nombre = models.CharField(max_length=100, unique=True)


class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    prioridad = models.IntegerField(max_length=20)
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Progreso', 'En Progreso'),
        ('Completada', 'Completada'),
    ]

    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')
    completada = models.BooleanField()
    fechacreacion = models.DateTimeField(default=timezone.now)
    horavencimiento = models.TimeField()
    
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tareas_creadas')

    usuarios_asignados = models.ManyToManyField(Usuario, through='AsignacionTarea', related_name='tareas_asignadas')

    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas')

    etiquetas = models.ManyToManyField(Etiqueta, related_name='tareas')

class AsignacionTarea(models.Model):
    observaciones = models.TextField(max_length=200)
    fechadeasignacion = models.DateField(default=timezone.now)
    
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)

class Comentario(models.Model):
    contenido = models.TextField(max_length=200)
    fecharegistro = models.DateTimeField(default=timezone.now)
    
    
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    # (Tarea que va con el comentario, no confudir)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='comentarios')
