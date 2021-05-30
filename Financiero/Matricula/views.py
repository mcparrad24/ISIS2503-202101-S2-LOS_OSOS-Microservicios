from django.shortcuts import render,redirect
from .models import Matricula
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json

def check_estudiante(data):
    r = requests.get(settings.PATH_EST, headers={"Accept":"application/json"})
    estudiantes = r.json()
    for estudiante in estudiantes:
        if data["estudianteEmail"] == estudiante["email"]:
            return True
    return False

def MatriculaList(request):
    queryset = Matricula.objects.all()
    context = list(queryset.values('id', 'periodo', 'factura', 'estudianteEmail'))
    return JsonResponse(context, safe=False)

def MatriculaCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if check_estudiante(data_json) == True:
            matricula = Matricula()
            matricula.id = data_json['id']
            matricula.id = data_json['periodo']
            matricula.id = data_json['factura']
            matricula.id = data_json['estudianteEmail']
            matricula.save()
            return HttpResponse("successfully created matricula")
        else:
            return HttpResponse("unsuccessfully created matricula. Estudiante does not exist")