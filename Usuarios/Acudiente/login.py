from django import forms

from Acudiente.models import Acudiente


class FormularioLogin(forms.ModelForm):
    class Meta:
        model=Acudiente
        fields= ["email","password"]
        widgets={"email": forms.EmailInput(), "password": forms.PasswordInput}