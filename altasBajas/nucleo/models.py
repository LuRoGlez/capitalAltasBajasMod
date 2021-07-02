from django.db import models


# Create your models here.

class Empresa (models.Model):
    nombre = models.CharField(max_length=50, unique=True)


    def __str__(self):
        return self.nombre

class Empleado (models.Model):
    nombre = models.CharField(max_length=100)
    empresa=models.ForeignKey(Empresa, verbose_name="Empresa", on_delete=models.CASCADE, related_name='empresa')

    class Vencimientos(models.TextChoices):
        ALTA = 'ALTA'
        BAJA = 'BAJA'
        BAJA51 = 'BAJA 51'
        BAJA93 = 'BAJA 93'
        BAJA85= 'BAJA 85'
        BAJA91 = 'BAJA 91'
        BAJA53 = 'BAJA 53'
        BAJA94 = 'BAJA 94'
        BAJA54 = 'BAJA 54'
        REDUCCION_JORNADA = 'REDUCCIÓN DE JORNADA'
        AMPLIACION_JORNADA = 'AMPLIACIÓN DE JORNADA'
        INACTIVIDAD = 'INACTIVIDAD'
        TRANSFORMACION = 'TRANSFORMACIÓN'
        PRORROGA = 'PROROGA'
        DESAFECTACION = 'DESAFECTACIÓN'
        LLAMAMIENTO = 'LLAMAMIENTO'
        BAJA_Y_ALTA = 'BAJA Y ALTA' 
   
    tipo_vencimiento = models.CharField(max_length=25, choices=Vencimientos.choices, blank=True)
    fechaBaja=models.DateField(null=True, blank = True)
    fechaAlta= models.DateField(null=True, blank = True)
    segSocial=models.BooleanField(default=False)
    sepe=models.BooleanField(default=False)
    enviadoContrato=models.BooleanField(default=False)
    sage=models.BooleanField(default=False)
    certificadoEmpresa=models.BooleanField(default=False)
    envioLiquidacion=models.BooleanField(default=False)
    firmaFY=models.BooleanField(default=False)
    class Asesores(models.TextChoices):
        Elena = 'Elena'
        JoseLuis = 'JoseLuis'
        Carmen = 'Carmen'
        Maria = 'Maria'
        Sara = 'Sara'
    asesor=models.CharField(max_length=25, choices=Asesores.choices, null=True, default="")

    def __str__(self):
        return " Empleado: "+self.nombre+" Empresa: "+self.empresa.nombre+" Tipo Vencimiento: "+self.tipo_vencimiento



