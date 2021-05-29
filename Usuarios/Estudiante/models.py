from django.db import models
# from Colegio.models import Colegio
# from Grupo.models import Grupo
# from Grado.models import Grado

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    colegio = models.CharField(max_length=50, null=True)
    codigo = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=10, null=True)
    grupo = models.CharField(max_length=50, null=True)
    grado = models.CharField(max_length=50, null=True)
    def __str__(self):
        return '{}'.format(self.nombre)