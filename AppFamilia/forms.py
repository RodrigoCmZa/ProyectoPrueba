from django import forms

    # Create your models here.
class EmpleadoForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fechaNacimiento = forms.DateField()
    ocupacion = forms.CharField(max_length=30)
    class Meta():
        ordering = ('apellido', 'nombre') # Ordena.
        unique_together = ('nombre', 'apellido', 'edad', 'fechaNacimiento') # No permite que se repitan.
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def str(self) -> str:
       return f'{self.apellido}, {self.nombre}'
    # Muestra en la pagina del Admin "apellido, nombre"


class TareasForm(forms.Form):
    nombre = forms.CharField(max_length=30) 
    dia_de_creacion = forms.DateTimeField(auto_now_add=True)
    responsable = forms.ForeignKey(EmpleadoForm, on_delete=forms.CASCADE)

    class Meta():
        ordering = ('dia_de_creacion', '-nombre', 'responsable') # Ordena.
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

    def str(self) -> str:
       return f'{self.dia_de_creacion}, {self.nombre}'
    # Muestra en la pagina del Admin "apellido, nombre"


class HerramientasForm(forms.Forms):
    nombre = forms.CharField(max_length=30)
    tipo_de_tarea = forms.ForeignKey(TareasForm, on_delete=forms.CASCADE)
    disponible =  forms.BooleanField()

    class Meta():
        ordering = ('nombre', 'tipo_de_tarea', 'disponible') # Ordena.
        verbose_name = 'Herramienta'
        verbose_name_plural = 'Herramientas'

    def str(self) -> str:
       return f'{self.dia_de_creacion}, {self.nombre}'
    # Muestra en la pagina del Admin "apellido, nombre"