# Generated by Django 3.2 on 2021-07-01 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0003_alter_empleado_asesor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='asesor',
            field=models.CharField(choices=[('Elena', 'Elena'), ('JoseLuis', 'Joseluis'), ('Carmen', 'Carmen'), ('Maria', 'Maria'), ('Sara', 'Sara')], default='', max_length=25, null=True),
        ),
    ]