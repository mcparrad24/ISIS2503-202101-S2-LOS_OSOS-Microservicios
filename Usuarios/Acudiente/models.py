from django.db import models

from Estudiante.models import Estudiante


class Acudiente(models.Model):
    nombre = models.CharField(max_length=50)
    estudiante = models.OneToOneField(Estudiante,on_delete=models.SET_NULL,primary_key=False, null=True)
    telefono = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, primary_key=True)
    password =models.CharField(max_length=10, null=True)
    def __str__(self):
        return '{}'.format(self.nombre)