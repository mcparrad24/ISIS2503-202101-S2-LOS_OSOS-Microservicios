from django.db import models
from Calificaciones.Asignacion.models import Asignacion
from UsuariosM.Estudiante.models import Estudiante

class Calificacion(models.Model):
    retroalimentacion = models.CharField(max_length=250)
    nota = models.FloatField(null=True, blank=True, default = None)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    asignacion = models.ForeignKey(Asignacion, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.nombre)
