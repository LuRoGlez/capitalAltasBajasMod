from .models import Empleado, Empresa
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django import forms
from datetime import datetime
from django.db.models import Q

now = datetime.now()

# Create your views here.
def meses(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    month = months[date.month -1]
    message = month
    return message

def index(request):
    return render(request, 'nucleo/index.html', {})

def EmpleadoList(request):
    queryset = request.GET.get("buscar")
    empleados=Empleado.objects.all()
    if queryset:
        empleados = Empleado.objects.filter(
            Q(nombre__icontains = queryset) |
            Q(fechaBaja__icontains = queryset) 
        ).distinct
    return render(request, "nucleo/empleado_list.html", {'empleados':empleados})

class EmpleadoCreateView(CreateView):
    model=Empleado
    fields=['nombre','empresa', 'tipo_vencimiento', 'fechaAlta', 'fechaBaja']
   
    success_url="/listEmpleado" 

class EmpleadoUpdateView(UpdateView):
    model=Empleado
    fields=['nombre', 'empresa', 'tipo_vencimiento', 'fechaAlta', 'fechaBaja', 'segSocial', 'sepe', 'enviadoContrato', 'sage', 'certificadoEmpresa', 'envioLiquidacion', 'firmaFY']
    
    success_url="/listEmpleado"

class EmpleadoDeleteView(DeleteView):
    model=Empleado
    success_url="/listEmpleado"

class EmpresaCreateView(CreateView):
    model=Empresa
    fields=('nombre', 'asesor')
    success_url="/listEmpleado" 


class EmpresaUpdateView(UpdateView):
    model=Empresa
    fields=['nombre', 'asesor']
    
    success_url="/listEmpresa"

class EmpresaListView(ListView):
    model=Empresa