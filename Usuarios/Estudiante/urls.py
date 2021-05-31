
from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^estudiantes/', views.EstudianteList, name='estudianteList'),
    url(r'^estudiantecreate/$', csrf_exempt(views.EstudianteCreate), name='estudianteCreate'),
]