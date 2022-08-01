from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from AppFamilia.models import Familia, Tareas
from django.views.decorators.http import require_GET, require_http_methods
from django.db.models import Q


# Create your views here.
# Codigo de Vitor Lira , PrimerMVT - Coder.


def Inicio(request):
    plantilla = loader.get_template("FamiliaInicio.html")
    documento = plantilla.render()
    return HttpResponse(documento)





@require_http_methods(["POST", "GET"])
def crear_persona(request):
    ctx = {"titulo": "Formulario de Familia"}
    if request.method == "POST":
        nombre = request.POST["nombre_familia"]
        apellido = request.POST["apellido_familia"]
        edad = request.POST["edad"]
        fechaNacimiento = request.POST["fechaNacimiento"]
        ocupacion = request.POST["ocupacion"]
        persona = Familia.objects.create(
            nombre = nombre, apellido=apellido,edad=edad,fechaNacimiento=fechaNacimiento,ocupacion=ocupacion
        )
        persona.save()

        messages.success(request, "Familia: " + nombre + " ¡Guardada con exito!")
        return redirect("/AppFamilia/familia/")
    return render(request, "formulario_padres.html", context=ctx)    
    
def mostrar_familia(request):
    personas = Familia.objects.all()
    ctx = {
        "titulo": "Lista de Personas",
        "personas": personas,
    }

    return render(request, "familia.html", context=ctx) 

@require_http_methods(["POST", "GET"])
def editar_persona(request, id):
    persona = Familia.objects.get(id=id)

    ctx = {"persona": persona, "titulo": "Formulario para editar persona"}
    if request.method == "POST":
        nombre = request.POST["nombre_familia"]
        apellido = request.POST["apellido_familia"]
        edad = request.POST["edad"]
        fechaNacimiento = request.POST["fechaNacimiento"]
        ocupacion = request.POST["ocupacion"]
        persona.nombre = nombre
        persona.apellido = apellido
        persona.edad = edad
        persona.fechaNacimiento = fechaNacimiento
        persona.ocupacion = ocupacion
        persona.save()
        messages.success(
            request, "Persona:" + nombre + " ¡Persona editada con éxito!"
        )
        return redirect("/AppFamilia/familia")

    return render(request, "editar_persona.html", context=ctx)


def eliminar_persona(request, id):
    
    persona = Familia.objects.get(id=id)
    persona.delete()
    messages.success(request, "¡Persona eliminada!")
    return redirect("/AppFamilia/familia")


def crear_tareas(request):
    ctx = {"titulo": "Formulario de tareas"}
    if request.method == "POST":
        nombre = request.POST["nombre_tarea"]
        responsable = request.POST["responsable"]
        tarea = Tareas.objects.create(
            nombre=nombre, responsables=responsable
        )  # noqa
        tarea.save()

        messages.success(request, "Tarea: " + nombre + " ¡Guardada con exito!")
        return redirect("/AppFamilia/tarea/")
    return render(request, "formulario_de_tarea.html", context=ctx)

# Vista basadas en funciones
# Vistas basadas en Clases


def mostrar_tarea(request):
    tareas = Tareas.objects.all()
    ctx = {
        "titulo": "Lista de tareas",
        "tareas": tareas,
    }

    return render(request, "tareas.html", context=ctx)




@require_http_methods(["POST", "GET"])
def editar_tareas(request, id):
    tarea = Tareas.objects.get(id=id)

    ctx = {"tarea": tarea, "titulo": "Formulario para editar tareas"}
    if request.method == "POST":
        nombre = request.POST["nombre_tarea"]
        responsable = request.POST["responsable"]
        tarea.nombre = nombre
        tarea.responsables = responsable
        tarea.save()
        messages.success(
            request, "Tarea:" + nombre + " ¡Tarea editada con éxito!"
        )
        return redirect("/AppFamilia/tarea")

    return render(request, "editar_tarea.html", context=ctx)


def eliminar_tarea(request, id):
    tarea = Tareas.objects.get(id=id)
    tarea.delete()
    messages.success(request, "¡Tarea eliminada!")
    return redirect("/AppFamilia/tarea")


def busqueda_familiar (request):
    return render(request, 'busqueda_familiar.html')


def buscar_persona(request):
    busqueda = request.GET.get("buscar")
    familiares = Familia.objects.all()  

    if busqueda:
        familiares = Familia.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(apellido__icontains = busqueda) |
            Q(edad__icontains = busqueda)|
            Q(fechaNacimiento__icontains = busqueda) |
            Q(ocupacion__icontains = busqueda)
        ).distinct()

        return render(request, 'resultado_busqueda.html', {'familiares':familiares})
    else:
        familiares = False
        return render(request, 'resultado_busqueda.html', {'familiares':familiares})