from django.urls import path

from AppFamilia.views import Inicio, Padres, Hermanos , Abuelos, read_tareas, crear_padres

# Codigo de Vitor Lira , PrimerMVT - Coder.

urlpatterns = [
    path('', Inicio),
    path('padres/',Padres),
    path('hermanos/', Hermanos),
    path('abuelos/', Abuelos),
    path('tarea/', read_tareas),
    path('padres/crear', crear_padres),
]
