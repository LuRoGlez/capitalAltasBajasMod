# Generated by Django 3.2 on 2021-07-08 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0011_auto_20210708_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='tipo_vencimiento',
            field=models.CharField(blank=True, choices=[('ALTA', 'Alta'), ('BAJA', 'Baja'), ('BAJA 51', 'Baja51'), ('BAJA 93', 'Baja93'), ('BAJA 85', 'Baja85'), ('BAJA 91', 'Baja91'), ('BAJA 53', 'Baja53'), ('BAJA 94', 'Baja94'), ('BAJA 54', 'Baja54'), ('REDUCCIÓN DE JORNADA', 'Reduccion Jornada'), ('AMPLIACIÓN DE JORNADA', 'Ampliacion Jornada'), ('INACTIVIDAD', 'Inactividad'), ('TRANSFORMACIÓN', 'Transformacion'), ('PROROGA', 'Prorroga'), ('DESAFECTACIÓN', 'Desafectacion'), ('LLAMAMIENTO', 'Llamamiento'), ('BAJA Y ALTA', 'Baja Y Alta')], default='BAJA', max_length=25),
        ),
    ]
