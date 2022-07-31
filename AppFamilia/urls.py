from django.urls import path

from AppFamilia.views import (
    Inicio,
    Padres,
    Hermanos,
    Abuelos,
    crear_tareas,
    editar_tareas,
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
]
