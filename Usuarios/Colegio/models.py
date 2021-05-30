from django.db import models

class Colegio (models.Model):
    id = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return '{}'.format(self.id)
