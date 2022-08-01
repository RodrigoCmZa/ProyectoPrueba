from django import forms

class TareasForm(forms.Form):
    nombre = forms.CharField()
    responsable = forms.CharField()
    
class FamiliaForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    fechaNacimiento = forms.DateField()
    ocupacion = forms.CharField()