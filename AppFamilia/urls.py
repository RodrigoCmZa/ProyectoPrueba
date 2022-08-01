from django.urls import path

from AppFamilia.views import (
    Inicio,
    crear_tareas,
    editar_tareas,
    eliminar_tarea,
    mostrar_tarea,
    crear_padres,
    mostrar_familia,
    editar_persona,
    eliminar_persona
)

# Codigo de Vitor Lira , PrimerMVT - Coder.

urlpatterns = [
    path("", Inicio),
    path("tarea/", mostrar_tarea, name='mostrar_tareas'),
    path("tarea/crear", crear_tareas, name='crear_tareas'),
    path("tarea/editar/<id>", editar_tareas, name='editar_tareas'),
    path("tarea/eliminar/<id>", eliminar_tarea, name='eliminar_tarea'),
    path("crear/padres", crear_padres, name="crear_persona"),
    path("familia/", mostrar_familia, name="mostrar_familia"),
    path("persona/editar/<id>", editar_persona, name='editar_persona'),
    path("persona/eliminar/<id>", eliminar_persona, name='eliminar_persona'),
]
