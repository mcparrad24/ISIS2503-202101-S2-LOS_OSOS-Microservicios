from django.db import models
from Colegio.models import Colegio
from Grupo.models import Grupo
from Grado.models import Grado

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=10, null=True)
    def __str__(self):
        return '{}'.format(self.email)