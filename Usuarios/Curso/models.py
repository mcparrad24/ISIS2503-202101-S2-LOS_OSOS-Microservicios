from django.db import models
from Estudiante.models import Estudiante
from Docente.models import Docente

class Curso (models.Model):
    id = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=255)
    estudiantes = models.ManyToManyField(Estudiante)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.id)
