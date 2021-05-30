from Factura.models import Factura
from django.db import models

class Matricula(models.Model):
    id = models.IntegerField(primary_key=True)
    periodo = models.CharField(max_length=255)
    factura = models.OneToOneField(Factura, on_delete=models.CASCADE, null=True)
    estudianteEmail = models.CharField(max_length=255, null = False, default = None)
    def __str__(self):
        return '{}'.format(self.id)
