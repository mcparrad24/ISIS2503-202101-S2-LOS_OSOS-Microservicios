from django.db import models

class Factura(models.Model):
    info = models.CharField(max_length=250)
    def __str__(self):
        return '{}'.format(self.nombre)
