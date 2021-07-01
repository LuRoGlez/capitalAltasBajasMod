from .models import Empleado, Empresa
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from .forms import FormularioCrearEmpleado
from django import forms

# Create your views here.

def index(request):
    return render(request, 'nucleo/index.html', {})

class EmpleadoListView(ListView):
    model=Empleado

class EmpleadoCreateView(CreateView):
    model=Empleado
    fields=['nombre', 'apellidos', 'empresa', 'tipo_vencimiento', 'fechaAlta', 'fechaBaja', 'asesor']
    widgets = {
            'fechaAlta': forms.SelectDateWidget(),
            'fechaBaja': forms.SelectDateWidget()
        } 
    success_url="/listEmpleado" 

class EmpleadoUpdateView(UpdateView):
    model=Empleado
    fields=['nombre', 'apellidos', 'empresa', 'tipo_vencimiento', 'fechaAlta', 'fechaBaja', 'asesor', 'segSocial', 'sepe', 'enviadoContrato', 'sage', 'certificadoEmpresa', 'envioLiquidacion', 'firmaFY']
    widgets = {
            'fechaAlta': forms.SelectDateWidget(),
            'fechaBaja': forms.SelectDateWidget()
        } 
    success_url="/listEmpleado"

class EmpleadoDeleteView(DeleteView):
    model=Empleado
    success_url="/listEmpleado"

class EmpresaCreateView(CreateView):
    model=Empresa
    fields=['nombre']
    success_url="/listEmpresa" 


