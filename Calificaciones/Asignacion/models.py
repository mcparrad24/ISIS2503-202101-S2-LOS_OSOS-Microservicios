from django.db import models
#from Curso.models import Curso
from UsuariosM.Estudiante.models import Estudiante

class Asignacion(models.Model):
    nombre = models.CharField(max_length=50)
    #curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)