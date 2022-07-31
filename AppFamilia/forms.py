from django import forms

class TareasForm(forms.Form):
    nombre = forms.CharField()
    responsable = forms.CharField()
    