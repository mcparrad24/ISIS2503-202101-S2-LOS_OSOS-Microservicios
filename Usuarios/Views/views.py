from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required

# from Calificacion.models import Calificacion
# from Docente.models import Docente
# from Estudiante.models import Estudiante
# from gnosoft.auth0backend import getRole, getID
# from Acudiente.forms import FormularioAcudiente
from django.contrib.auth import logout as log_out
from django.conf import settings
from urllib.parse import urlencode

def home(self):
    plantilla=get_template('index.html')
#    acudientes = Acudiente.objects.all()
#    html+= '<\n>'.join(["nombre: %s"% (a.nombre)for a in acudientes])
    return HttpResponse(plantilla.render())
def formulario(self):
    plantilla=get_template('formulario.html')
    return HttpResponse(plantilla.render())

# def login(request):
#     role=getRole(request)
#     id=getID(request)
#
#     if role=="Profesor":
#         u = Docente.objects.get(id=id)
#         plantilla=get_template('profesor.html')
#         return HttpResponse(plantilla.render({"usuario": u}))
#     elif role=="Estudiante":
#         u=Estudiante.objects.get(id=id)
#         notas=Calificacion.objects.get(estudiante=id)
#         plantilla = get_template('estudiante.html')
#         return HttpResponse(plantilla.render({"usuario": u, "notas": notas}))
#     # return HttpResponse(plantilla.render({"usuario":u, "notas":notas}))
#
# def logout(request):
#     print('---------------')
#     log_out(request)
#     return_to = urlencode({'returnTo':request.build_absolute_uri('/')})
#     # logout_url = 'https://%s/v2/logout?client_id=%s&%s'% \
#     #     #              (settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
#     logout_url="https://dev-34eki5-n.us.auth0.com/v2/logout?returnTo="+return_to
#     print('return',return_to)
#     print(logout_url)
#     return HttpResponseRedirect(logout_url)