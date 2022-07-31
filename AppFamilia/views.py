from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from AppFamilia.models import Familia, Tareas
from django.views.decorators.http import require_GET, require_http_methods

# Create your views here.
# Codigo de Vitor Lira , PrimerMVT - Coder.


def Inicio(request):
    plantilla = loader.get_template("FamiliaInicio.html")
    documento = plantilla.render()
    return HttpResponse(documento)


@require_GET
def Padres(request):
    ctx = {
        "nombre": "Sara",
        "apellido": "Goldstein",
        "edad": 36,
        "fechaNacimiento": "1986-07-27",
        "ocupacion": "Enfermera",
    }
    return render(request, "padres.html", context=ctx)


@require_http_methods(["POST", "GET"])
def crear_padres(request):
    if request.method == "POST":
        madre = Familia(
            nombre="Sara",
            apellido="Goldstein",
            edad=36,
            fechaNacimiento="1986-07-27",
            ocupacion="Enfermera",
        )
        plantilla = loader.get_template("padres.html")
        documentoTexto = {
            "nombre": madre.nombre,
            "apellido": madre.apellido,
            "edad": madre.edad,
            "fn": madre.fechaNacimiento,
            "ocupacion": madre.ocupacion,
        }
        documento = plantilla.render(documentoTexto)
        return HttpResponse(documento)
    return render(request, "formulario_padres.html")


@require_http_methods(["POST", "GET"])
def Hermanos(request):
    if request.method == "POST":
        hermana = Familia(
            nombre="Martina",
            apellido="Goldstein",
            edad=7,
            fechaNacimiento="2015-01-25",
            ocupacion="Estudiante",
        )
        plantilla = loader.get_template("hermanos.html")
        documentoTexto = {
            "nombre": hermana.nombre,
            "apellido": hermana.apellido,
            "edad": hermana.edad,
            "fn": hermana.fechaNacimiento,
            "ocupacion": hermana.ocupacion,
        }
        documento = plantilla.render(documentoTexto)
        return HttpResponse(documento)
    return render(request, "hermanos.html")


@require_http_methods(["POST", "GET"])
def Abuelos(request):
    if request.method == "POST":
        abuela = Familia(
            nombre="Maria",
            apellido="Goldstein",
            edad=59,
            fechaNacimiento="1963-02-04",
            ocupacion="Jubilada",
        )
        plantilla = loader.get_template("abuelos.html")
        documentoTexto = {
            "nombre": abuela.nombre,
            "apellido": abuela.apellido,
            "edad": abuela.edad,
            "fn": abuela.fechaNacimiento,
            "ocupacion": abuela.ocupacion,
        }
        documento = plantilla.render(documentoTexto)
        return HttpResponse(documento)


# Vista basadas en funciones
# Vistas basadas en Clases


  

def mostrar_tarea(request):
    tareas = Tareas.objects.all()
    ctx = {
        "titulo": "Lista de tareas",
        "tareas": tareas,
        
    }
    
    return render(request, "tareas.html", context=ctx)   



def crear_tareas(request):
    ctx = {"titulo": "Formulario de tareas"}
    if request.method == "POST":
        nombre = request.POST["nombre_tarea"]
        responsable = request.POST["responsable"]
        tarea = Tareas.objects.create(nombre=nombre, responsables=responsable)  # noqa
        tarea.save()

        messages.success(request, "Tarea: " + nombre + " ¡Guardada con exito!")
        return redirect("/AppFamilia/tarea/")
    return render(request, "formulario_de_tarea.html", context=ctx)


@require_http_methods(["POST", "GET"])
def editar_tareas(request, id):
    tarea = Tareas.objects.get(id=id)
    
    ctx= {"tarea": tarea, 'titulo': "Formulario para editar tareas"}
    if request.method == 'POST':
        nombre = request.POST['nombre_tarea']
        print("Hola mundo")
        responsable = request.POST['responsable']
        tarea.nombre=nombre
        tarea.responsables=responsable
        tarea.save()
        messages.success(request, 'Tarea:' + nombre +' ¡Tarea editada con éxito!')
        return redirect("/AppFamilia/tarea")
        

    return render(request, "editar_tarea.html", context=ctx)