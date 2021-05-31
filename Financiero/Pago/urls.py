
from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^pagos/', views.PagoList),
    url(r'^pagocreate/$', csrf_exempt(views.PagoCreate), name='pagoCreate'),
]