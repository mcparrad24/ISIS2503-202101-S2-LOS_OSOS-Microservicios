from django.db import models
#from Colegio.models import Colegio

class Docente(models.Model):
    nombre = models.CharField(max_length=50)
    colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}'.format(self.nombre)
