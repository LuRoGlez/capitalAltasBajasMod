from django import forms
from django.forms import widgets
from .models import Empleado, Empresa

class FormularioCrearEmpleado (forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ('nombre', 'apellidos', 'empresa', 'tipo_vencimiento', 'fechaAlta', 'fechaBaja', 'asesor')
        widgets = {
            'fechaAlta': forms.DateInput(),
            'fechaBaja': forms.DateInput()
        }