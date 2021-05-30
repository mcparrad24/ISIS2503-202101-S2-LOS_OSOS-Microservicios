from django.db import models
from Pago.models import Pago

class Factura(models.Model):
    id = models.IntegerField(primary_key=True)
    info = models.CharField(max_length=255)
    pago = models.OneToOneField(Pago, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.id)
