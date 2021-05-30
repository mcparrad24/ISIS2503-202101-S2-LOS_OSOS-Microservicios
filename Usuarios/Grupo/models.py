from django.db import models
from Grado.models import Grado

class Grupo(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.id)
