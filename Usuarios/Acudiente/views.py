# import objects as objects
from django.http import HttpRequest

from Acudiente.forms import FormularioAcudiente
from Acudiente.login import FormularioLogin
from Acudiente.models import Acudiente

from .models import Variable
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json

class FormularioAcudienteView(HttpRequest):

    def index(request):
        acudiente = FormularioAcudiente()
        return render(request, "AcudienteIndex.html", {"form": acudiente})

    def procesar_formulario(request):
        acudiente = FormularioAcudiente(request.POST)
        if acudiente.is_valid():
            acudiente.save()
            acudiente = FormularioAcudiente()
        return render(request, "AcudienteIndex.html", {"form": acudiente, "mensaje": "ok"})

    def log(request):
        acudiente = FormularioLogin()
        return render(request, "formulario.html", {"form": acudiente})

    def login(request):
        acudiente = FormularioLogin(request.POST)
        mensaje = ""
        error = ""
        if acudiente.data.get('email'):
            mail = acudiente.data.get('email')
            a = Acudiente.objects.get(email=mail)
            if acudiente.data.get('password') == a.password:
                mensaje = "ok"
            else:
                error = "Hay"
        acudiente = FormularioLogin
        return render(request, "formulario.html",
                      {"form": acudiente, "mensaje": mensaje, "error": error, "acudiente": a})

    def info(request, a):
        acudiente=Acudiente.objects.get(email=a)
        return render(request, "infoAcudiente.html", {"acudiente": acudiente})

def AcudienteList(request):
    queryset = Acudiente.objects.all()
    context = list(queryset.values('nombre', 'estudiante', 'telefono', 'email', 'password'))
    return JsonResponse(context, safe=False)

def AcudienteCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        acudiente = Acudiente()
        acudiente.email = data_json["email"]
        acudiente.save()
        return HttpResponse("successfully created variable")