from django import forms

from Acudiente.models import Acudiente


class FormularioAcudiente(forms.ModelForm):
    class Meta:
        model=Acudiente
        fields='__all__'
        widgets={"email": forms.EmailInput(), "password": forms.PasswordInput}
