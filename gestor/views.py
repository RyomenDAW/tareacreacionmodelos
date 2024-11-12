
# Create your views here.
from django.shortcuts import render
from .models import Proyecto,Tarea, Usuario, AsignacionTarea, Comentario, Etiqueta

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

def ultimo_comentario_usuario_proyecto(request, id_proyecto):
    # Obtener la primera tarea asociada al proyecto
    tarea = Tarea.objects.filter(proyecto_id=id_proyecto).first()

    # Obtener el último comentario de la tarea, si existe
    if tarea:
        comentario = tarea.comentarios.order_by('-fecharegistro').first()
    else:
        comentario = None  # No hay tarea

    # Retornar el template con el comentario (o sin él)
    return render(request, 'tareas/ultimo_comentario_usuario_proyecto.html', {'comentario': comentario})



    
# Crear una URL que obtenga todos los comentarios de una tarea que empiecen por la palabra que se pase en la URL y que el año del comentario sea uno en concreto.

def todoscomentarios_palabraurl_añocomentario(request, palabra, año):
    comentarios = Comentario.objects.filter(
        contenido__startswith=palabra,
        fecharegistro__year=año
    )

    # Retornar el template con la lista de comentarios
    return render(request, 'tareas/todoscomentarios_palabraurl_añocomentario.html', {'comentarios': comentarios, 'palabra': palabra, 'año': año})

# Crear una URL que obtenga todas las etiquetas que se han usado en todas las tareas de un proyecto.
def etiquetas_todastareas_proyecto(request, id_proyecto):
  tareas = Tarea.objects.filter(proyecto_id=id_proyecto)
    # Obtener todas las etiquetas usadas en las tareas de este proyecto
  etiquetas = Etiqueta.objects.filter(tareas__in=tareas).distinct()
    # Retornar la plantilla con las etiquetas
  return render(request, 'etiquetas/etiquetas_todastareas_proyecto.html', {'etiquetas': etiquetas})
# Crear una URL que muestre todos los usuarios que no están asignados a una tarea.


def usuariosnoasignados_tarea(request, id_tarea):
    tarea = Tarea.objects.get(id=id_tarea)
    usuarios = Usuario.objects.all()
    usuarios_asignados = tarea.usuarios_asignados.all()  # related name

    # Filtrar los usuarios que no están asignados a la tarea
    usuariosnoasignados_tarea = usuarios.exclude(id__in=usuarios_asignados.values_list('id', flat=True))
    return render(request, 'usuarios/usuariosnoasignados_tarea.html', {'usuariosnoasignados_tarea': usuariosnoasignados_tarea})

# Crear una página de Error personalizada para cada uno de los 4 tipos de errores que pueden ocurrir en nuestra Web.

def error_400_view(request, exception):
    return render(request, '../template/errors/400.html', status=400)

def error_403_view(request, exception):
    return render(request, '../template/errors/403.html', status=403)

def error_404_view(request, exception):
    return render(request, '../template/errors/404.html', status=404)

def error_500_view(request):
    return render(request, '../template/errors/500.html', status=500)