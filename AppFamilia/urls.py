from django.urls import path

from AppFamilia.views import (
    Inicio,
    Padres,
    Hermanos,
    Abuelos,
    crear_tareas,
    editar_tareas,
    eliminar_tarea,
    mostrar_tarea,
    crear_padres,
)

# Codigo de Vitor Lira , PrimerMVT - Coder.

urlpatterns = [
    path("", Inicio),
    path("padres/", Padres),
    path("padres/crear", crear_padres),
    path("hermanos/", Hermanos),
    path("abuelos/", Abuelos),
    path("tarea/", mostrar_tarea, name='mostrar_tareas'),
    path("tarea/crear", crear_tareas, name='crear_tareas'),
    path("tarea/editar/<id>", editar_tareas, name='editar_tareas'),
    path("tarea/eliminar/<id>", eliminar_tarea, name='eliminar_tarea'),
]
