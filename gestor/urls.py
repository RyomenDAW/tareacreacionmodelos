from django.urls import path
from .views import inicio, lista_proyectos, lista_tareas, lista_usuarios, lista_tareas_textoconcreto, lista_tareas_completadas, ultimo_comentario_usuario_proyecto, todoscomentarios_palabraurl_añocomentario, etiquetas_todastareas_proyecto, usuariosnoasignados_tarea
from django.conf.urls import handler400, handler403, handler404, handler500
from gestor.views import error_400_view, error_403_view, error_404_view, error_500_view
from . import views
from django.conf.urls import handler400, handler403, handler404, handler500

handler400 = "gestor.views.error400_view"
handler403 = "gestor.views.error403_view"
handler404 = "gestor.views.error404_view"
handler500 = "gestor.views.error500_view"

urlpatterns = [
    path('inicio.html', views.inicio, name='inicio'),
    
    
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

    path('tareas/<int:id_proyecto>/', ultimo_comentario_usuario_proyecto, name='ultimo_comentario_usuario_proyecto'),
    
    #     Crear una URL que obtenga todos los comentarios de una tarea que empiecen por la palabra que se pase en la URL y que el año del comentario sea uno en concreto.
    path('comentarios/<str:palabra>/<int:año>/', todoscomentarios_palabraurl_añocomentario, name='todoscomentarios_palabraurl_añocomentario'),


    # Crear una URL que obtenga todas las etiquetas que se han usado en todas las tareas de un proyecto.
    path('etiquetas/<int:id_proyecto>/', etiquetas_todastareas_proyecto, name='etiquetas_todastareas_proyecto'),
    # Crear una URL que muestre todos los usuarios que no están asignados a una tarea.

    path ('usuarios/<int:id_tarea>/', usuariosnoasignados_tarea, name='usuariosnoasignados_tarea'),
    # Crear una página de Error personalizada para cada uno de los 4 tipos de errores que pueden ocurrir en nuestra Web.

]   

