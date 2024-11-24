# tareacreacionmodelos
Tarea de Creacion Modelos, 13 Octubre



.....
El script es un alert, la imagen es soul of cinder, el css cambia esto:

h1{
    color: blue;
}


p{
    color: red;
}

==========================================================================================================================================


## Template Tags Utilizados

```django
{% comment %} AQUI VA EL PRIMER TEMPLATE TAG, UN IF ELSE {% endcomment %}

{% if tareas %}
<ul>
    {% for asignaciontarea in tareas %}
        {% include "../estructura/asignaciontarea_for.html" %}
    {% empty %}
        <p>No hay tareas asignadas en este momento.</p>
    {% endfor %}
</ul>
{% else %}
<p>No hay tareas disponibles para mostrar.</p>
{% endif %}

{% comment %} FIN DEL PRIMER TEMPLATE TAG {% endcomment %}


{% comment %} ESTE ES EL SEGUNDO TEMPLATE TAG, FOR EMPTY {% endcomment %}

{% for tarea in tareas %}
    {% include "../estructura/tarea_for.html" %}
{% empty %}
    <p>No hay tareas actualmente, no puedo mostrarte la lista</p>
{% endfor %}

{% comment %} FIN DEL SEGUNDO TEMPLATE TAG {% endcomment %}


{% comment %} TERCER TEMPLATE TAG, INCLUDE {% endcomment %}

{% include './footer.html' %}

{% comment %} FIN DEL TERCER TEMPLATE TAG {% endcomment %}



{% comment %} CUARTO TEMPLATE TAG: BLOCK Y ENDBLOCK {% endcomment %}

{% block contenido %}
{% endblock %}

{% comment %} FIN DEL CUARTO TEMPLATE TAG {% endcomment %}



{% comment %} QUINTO TEMPLATE TAG, FOR, ENDFOR {% endcomment %}

{% for comentario in comentarios %}
    {% include "../estructura/comentario_for.html" %}
{% endfor %}

{% comment %} FIN DEL QUINTO TEMPLATE TAG {% endcomment %}

==========================================================================================================================================
Operadores usados:
{% comment %} PRIMER OPERADOR, IGUALDAD == {% endcomment %}
{% comment %} SEGUNDO Y TERCER OPERADOR, ARITMÉTICOS > Y < {% endcomment %}
{% comment %} CUARTO OPERADOR, `if not` {% endcomment %}
{% comment %} QUINTO OPERADOR, ES UN `AND` {% endcomment %}

==========================================================================================================================================

Filtros de Plantilla Utilizados
1. upper
Convierte todo el texto a mayúsculas.

2. slice
Extrae una porción de una cadena de texto o lista. Se puede utilizar para tomar un número específico de caracteres o elementos.

3. default_if_none
Proporciona un valor por defecto solo si el valor original es None.

4. lower
Convierte todo el texto a minúsculas.

5. truncatewords
Trunca el texto a un número específico de palabras. Es útil cuando se necesita limitar la longitud del texto mostrado.

6. date
Formatea un objeto datetime en una cadena de texto con un formato específico. Permite mostrar fechas de forma legible.

7. length
Devuelve la longitud de una lista, cadena o iterable. Es útil para mostrar el tamaño de una colección o cadena.

8. title
Convierte la primera letra de cada palabra en mayúscula. Ideal para títulos o nombres de campos.

9. default
Proporciona un valor por defecto si la variable es vacía o None. Se usa para asegurar que siempre haya un valor visible en caso de que no exista uno.

10. add
Suma un valor al original. Puede utilizarse para realizar cálculos dentro de las plantillas.

Cómo usar los filtros
Estos filtros pueden ser aplicados a cualquier variable dentro de las plantillas de Django para modificar su formato, mostrar valores predeterminados, o realizar operaciones como sumar valores. Solo es necesario usar el operador de filtro |, seguido del nombre del filtro y sus parámetros si los hubiera (como en el caso de truncatewords:10 o date:"d M Y").

