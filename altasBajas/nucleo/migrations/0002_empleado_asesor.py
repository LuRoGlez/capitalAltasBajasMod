# Generated by Django 3.2 on 2021-06-29 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='asesor',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
