from .models import Pago
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json

def check_acudiente(data):
    r = requests.get(settings.PATH_ACU, headers={"Accept":"application/json"})
    acudientes = r.json()
    for acudiente in acudientes:
        if data["acudienteEmail"] == acudiente["email"]:
            return True
    return False

def PagoList(request):
    queryset = Pago.objects.all()
    context = list(queryset.values('id', 'descripcion', 'acudienteEmail'))
    return JsonResponse(context, safe=False)

def PagoCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if check_acudiente(data_json) == True:
            pago = Pago()
            pago.id = data_json['id']
            pago.id = data_json['descripcion']
            pago.id = data_json['acudienteEmail']
            pago.save()
            return HttpResponse("successfully created pago")
        else:
            return HttpResponse("unsuccessfully created pago. Acudiente does not exist")