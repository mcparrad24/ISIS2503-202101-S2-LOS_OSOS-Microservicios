from django.db import models

class Pago(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    acudienteEmail = models.CharField(max_length=255, null = False, default = None)
    def __str__(self):
        return '{}'.format(self.id)