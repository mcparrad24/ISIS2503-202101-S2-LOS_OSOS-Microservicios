from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

# from Acudiente.forms import FormularioAcudiente


def home(self):
    plantilla=get_template('index.html')
#    acudientes = Acudiente.objects.all()
#    html+= '<\n>'.join(["nombre: %s"% (a.nombre)for a in acudientes])
    return HttpResponse(plantilla.render())
def formulario(self):
    plantilla=get_template('formulario.html')
    return HttpResponse(plantilla.render())
