from django.db import models
from UsuariosM.Estudiante.models import Estudiante

class Boletin(models.Model):
    periodo = models.CharField(max_length=50)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.nombre)
