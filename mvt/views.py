from django.http import HttpResponse
from django.template import Template,Context
from django.template import loader

def Inicio(request):
    plantilla = loader.get_template('inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def Prueba(request):
    return HttpResponse("Hola")