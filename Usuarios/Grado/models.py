from django.db import models

class Grado(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return '{}'.format(self.id)
