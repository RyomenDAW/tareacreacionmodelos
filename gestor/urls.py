from django.urls import path
from .views import inicio, lista_proyectos, lista_tareas, lista_usuarios, lista_tareas_textoconcreto

urlpatterns = [
    path('', inicio, name='inicio'),  # Página de inicio
    path('proyectos/', lista_proyectos, name='lista_proyectos'),  # URL para la lista de proyectos
    
    
    # Crear una URL que muestre todas las tareas que están asociadas a un proyecto, ordenadas por
    # fecha de creación descendente.
    path('tareas/', lista_tareas, name='lista_tareas'),  # URL para la lista de todas las tareas
    
    
    #Crear una URL que muestre todos los usuarios que están asignados a una tarea ordenados por la fecha de asignación de la tarea de forma ascendente. 
    path('usuarios/', lista_usuarios, name='lista_usuarios') 
    
    #Crear una URL que muestre todas las tareas que tengan un texto en concreto en las 
    # observaciones a la hora de asignarlas a un usuario.

    path ('tareas/', lista_tareas_textoconcreto, name='lista_tareas_textoconcreto')
    
]