from datetime import datetime
from django.db import models

# Create your models here.
class Empleados(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fechaNacimiento = models.DateField()
    ocupacion = models.CharField(max_length=30)
    class Meta():
        ordering = ('apellido', 'nombre') # Ordena.
        unique_together = ('nombre', 'apellido', 'edad', 'fechaNacimiento') # No permite que se repitan.
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
       return f'{self.nombre} {self.apellido}'
    # Muestra en la pagina del Admin "apellido, nombre"


class Tareas(models.Model):
    nombre = models.CharField(max_length=30) 
    dia_de_creacion = models.DateTimeField()
    responsable = models.ForeignKey(Empleados, on_delete=models.CASCADE,null=True,blank=True)

    class Meta():
        ordering = ('dia_de_creacion', '-nombre', 'responsable') # Ordena.
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

    def __str__(self) -> str:
       return f'{self.dia_de_creacion}, {self.nombre}'
    # Muestra en la pagina del Admin "apellido, nombre"


class Herramientas(models.Model):
    nombre = models.CharField(max_length=30)
    tipo_de_tarea = models.ForeignKey(Tareas, on_delete=models.CASCADE,null=True,blank=True)
    disponible =  models.BooleanField(default=False)

    class Meta():
        ordering = ('nombre', 'tipo_de_tarea') # Ordena.
        verbose_name = 'Herramienta'
        verbose_name_plural = 'Herramientas'

    def __str__(self) -> str:
        return f'{self.dia_de_creacion}, {self.nombre}'
    # Muestra en la pagina del Admin "apellido, nombre"