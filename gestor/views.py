
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Proyecto,Tarea, Usuario, AsignacionTarea
from django.db.models import Q, Prefetch

def inicio(request):
    return render(request, 'inicio.html')

def lista_proyectos(request):
    proyectos = Proyecto.objects.all()  # Recuperar todos los proyectos
    return render(request, 'proyectos/lista_proyectos.html', {'proyectos': proyectos})

# Crear una URL que muestre todas las tareas que están asociadas a un proyecto, 
# ordenadas por fecha de creación descendente.ç


#==========================00

def lista_tareas(request):
    # Obtener todas las tareas y ordenarlas por fecha de creación (descendente)
    tareas = Tarea.objects.all().order_by('-fechacreacion')  # Elimina la coma al final
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})

# Crear una URL que muestre todas las tareas que están asociadas a un proyecto,
# ordenadas por fecha de creación descendente.

def lista_usuarios(request):
    # Obtener todas las asignaciones y ordenarlas por fecha de asignación (ascendente)
    asignaciones = AsignacionTarea.objects.all().order_by('fechadeasignacion')

    # Extraer los usuarios de las asignaciones
    usuarios = [asignacion.usuario for asignacion in asignaciones]

    # Renderizar la plantilla con los usuarios
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})




#Crear una URL que muestre todas las tareas que tengan un texto en 
# concreto en las observaciones a la hora de asignarlas a un usuario.

def lista_tareas_textoconcreto(request, texto_observacion):
    tareas = AsignacionTarea.objects.all().filter(observaciones__icontains=texto_observacion)
    return render(request, 'tareas/lista_tareas_textoconcreto.html', {'tareas': tareas})


# Crear una URL que muestre todos las tareas que se han creado entre dos años y el estado sea “Completada”.

# En views.py
def lista_tareas_completadas(request, anio_inicio, anio_fin):
    tareas = Tarea.objects.filter(
        fechacreacion__year__range=(anio_inicio, anio_fin),
        estado='Completada'
    )
    return render(request, 'tareas/lista_tareas_completadas.html', {'tareas': tareas})
#Crear una URL que obtenga el último usuario que ha comentado en una tarea de un proyecto en concreto.

def ultimo_comentario_usuario_proyecto(request):
    tareas = Tarea.objects.prefetch_related(Prefetch"tarea_usuarios_asignados").get(id=id.Proyecto)