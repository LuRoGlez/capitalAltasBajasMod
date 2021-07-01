
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name="index"),
    path('listEmpleado',views.EmpleadoListView.as_view(), name="listEmpleado"),
    path('createEmpleado',views.EmpleadoCreateView.as_view(), name="createEmpleado"),
    path('updateEmpleado/<int:pk>',views.EmpleadoUpdateView.as_view(), name="updateEmpleado"),
    path('deleteEmpleado/<int:pk>',views.EmpleadoDeleteView.as_view(), name="deleteEmpleado"),
    path('createEmpresa',views.EmpresaCreateView.as_view(), name="createEmpresa"),
   
]