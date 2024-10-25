from django.urls import path
from .views import inicio, lista_proyectos, lista_tareas, lista_usuarios, lista_tareas_textoconcreto, lista_tareas_completadas, ultimo_comentario_usuario_proyecto

urlpatterns = [
    path('', inicio, name='inicio'),  # Página de inicio
    path('proyectos/', lista_proyectos, name='lista_proyectos'),  # URL para la lista de proyectos
    
    
    # Crear una URL que muestre todas las tareas que están asociadas a un proyecto, ordenadas por
    # fecha de creación descendente.
    path('tareas/', lista_tareas, name='lista_tareas'),  # URL para la lista de todas las tareas
    
    
    #Crear una URL que muestre todos los usuarios que están asignados a una tarea ordenados por la fecha de asignación de la tarea de forma ascendente. 
    path('usuarios/', lista_usuarios, name='lista_usuarios'),
    
    #Crear una URL que muestre todas las tareas que tengan un texto en concreto en las 
    # observaciones a la hora de asignarlas a un usuario.

    path('tareas/textoconcreto/', lista_tareas_textoconcreto, name='lista_tareas_textoconcreto'),
    
    
    #Crear una URL que muestre todos las tareas que se han creado entre dos años y el
    #estado sea “Completada”.
    
    path('tareas/<int:anio_inicio>/<int:anio_fin>/', lista_tareas_completadas, name='lista_tareas_completadas'),

    # Crear una URL que obtenga el último usuario que ha comentado en una tarea de un 
    # proyecto en concreto.

    path('tareas/<int:id_proyecto>/', ultimo_comentario_usuario_proyecto, name='ultimo_comentario_usuario_proyecto')
]