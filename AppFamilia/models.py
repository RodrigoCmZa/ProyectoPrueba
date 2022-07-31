from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fechaNacimiento = models.DateField()
    ocupacion = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    

class Tareas(models.Model):
    nombre = models.CharField(max_length=30) 
    responsables = models.CharField(max_length=30)
    dia_de_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

    def __str__(self):
        return f'{self.nombre}' 



class Herramientas(models.Model):
    nombre = models.CharField(max_length=30)
    tipo_de_tarea = models.CharField(max_length=30)
    responsable_de_uso = models.CharField(max_length=30)
    is_used =  models.BooleanField()