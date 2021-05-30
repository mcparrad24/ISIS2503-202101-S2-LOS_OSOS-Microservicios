from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^matriculas/', views.MatriculaList),
    url(r'^matyriculacreate/$', csrf_exempt(views.MatriculaCreate), name='matriculaCreate'),
]