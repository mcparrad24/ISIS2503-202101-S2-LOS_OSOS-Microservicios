
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from Estudiante.login import FormularioLogin
from Estudiante.models import Estudiante

from django.core.files.storage import FileSystemStorage
#from .forms import ModelFormWithFileField
from django.http import HttpResponseRedirect
from django.http import HttpResponse




class FormularioEstudianteView(HttpRequest):
    def log(request):
        estudiante = FormularioLogin()
        return render(request, "formularioEstudiante.html", {"form": estudiante})


    def login(request):
        estudiante = FormularioLogin(request.POST)
        mensaje = ""
        error = ""
        if estudiante.data.get('email'):
            mail = estudiante.data.get('email')
            a = Estudiante.objects.get(email=mail)
            if estudiante.data.get('password') == a.password:
                mensaje = "ok"
            else:
                error = "Hay"
        estudiante = FormularioLogin
        return render(request, "formularioEstudiante.html",
                      {"form": estudiante, "mensaje": mensaje, "error": error, "estudiante": a})


    def info(request, a):
        estudiante = Estudiante.objects.get(email=a)
        return render(request, "infoEstudiante.html", {"estudiante": estudiante})

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'upload.html')

def upload_redirect(request):
    return redirect('upload.html')