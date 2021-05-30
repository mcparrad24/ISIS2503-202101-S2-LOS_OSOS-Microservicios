from django.db import models
from Colegio.models import Colegio

class Docente (models.Model):
    email = models.CharField(max_length=255, primary_key = True)
    nombre = models.CharField(max_length=255)
    colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.email)
