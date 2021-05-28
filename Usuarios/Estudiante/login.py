from django import forms

from Acudiente.models import Acudiente
from Estudiante.models import Estudiante


class FormularioLogin(forms.ModelForm):
    class Meta:
        model=Estudiante
        fields= ["email","password"]
        widgets={"email": forms.EmailInput(), "password": forms.PasswordInput}
