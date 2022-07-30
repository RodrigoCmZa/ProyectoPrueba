import datetime

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.template import Template,Context
from django.template import loader
from AppFamilia.models import Familia, Tareas, Herramientas
from django.views.decorators.http import require_GET, require_http_methods
# Create your views here.
# Codigo de Vitor Lira , PrimerMVT - Coder.

def Inicio(request):
    plantilla = loader.get_template('FamiliaInicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)
    
@require_GET 
def Padres(request):
    ctx ={'nombre': "Sara", 'apellido': "Goldstein", 'edad': 36, 'fechaNacimiento' :'1986-07-27', 'ocupacion':  "Enfermera"}
    return render(request, 'padres.html', context= ctx)
    

@require_http_methods(["POST", "GET"])
def crear_padres(request):
    if  request.method == 'POST':
        madre = Familia(nombre = "Sara", apellido= "Goldstein", edad = 36, fechaNacimiento = "1986-07-27", ocupacion = "Enfermera")
        plantilla = loader.get_template('padres.html')
        documentoTexto = {'nombre': madre.nombre,'apellido': madre.apellido,'edad':madre.edad,'fn':madre.fechaNacimiento,'ocupacion':madre.ocupacion }
        documento = plantilla.render(documentoTexto)
        return HttpResponse(documento)
    return render(request, 'formulario_padres.html')

def Hermanos(request):
    hermana = Familia(nombre = "Martina", apellido= "Goldstein", edad = 7, fechaNacimiento = "2015-01-25", ocupacion = "Estudiante")
    hermana.save()
    plantilla = loader.get_template('hermanos.html')
    documentoTexto = {'nombre': hermana.nombre, 'apellido': hermana.apellido,'edad':hermana.edad,'fn':hermana.fechaNacimiento,'ocupacion':hermana.ocupacion}
    documento = plantilla.render(documentoTexto)
    return HttpResponse(documento)

def Abuelos(request):
    abuela = Familia(nombre = "Maria", apellido= "Goldstein", edad = 59, fechaNacimiento = "1963-02-04", ocupacion = "Jubilada")
    abuela.save()
    plantilla = loader.get_template('abuelos.html')
    documentoTexto = {'nombre': abuela.nombre,'apellido': abuela.apellido,'edad':abuela.edad,'fn':abuela.fechaNacimiento,'ocupacion':abuela.ocupacion}
    documento = plantilla.render(documentoTexto)
    
    return HttpResponse(documento)

# Vista basadas en funciones
# Vistas basadas en Clases

def read_tareas(request):
    plantilla = loader.get_template('tareas.html')
    context = {'nombre': 'esta es la tarea uno', 'responsable': 'este seria el responsable', 'dia_de_creacion': 'Este es el dia de creacion'}
    documento = plantilla.render(context)
    return HttpResponse(documento)
    
def create_tarea(request):
    nombre = request.POST['nombre'] 
    responsable = request.POST['responsable']
    dia_de_creacion = request.POST['dia_de_creacion']
    tarea = Tareas.objects.create(
        nombre=nombre,
        responsable=responsable,
        dia_de_creacion=dia_de_creacion
    )
    messages.success(request, 'Tarea: ' + nombre +' ¡Guardada con exito!')
    return redirect('/tareas/')