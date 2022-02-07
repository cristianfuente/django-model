from django import forms
from .models import Persona
BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
class RegistroForm(forms.ModelForm):
    class Meta:
        model=Persona
        fields=[
            'nombres',
            'apellidos',
            'idTipoDoc',
            'documento',
            'LugarResidencia',
            'fechanacimiento',
            'email',
            'telefono',
            'usuario',
            'password',
        ]
        widgets={
            'nombres':forms.TextInput(attrs={'class': 'form-control', 'required': 'required','placeholder':'Nombres completos'}),
            'apellidos':forms.TextInput(attrs={'class': 'form-control', 'required': 'required','placeholder':'Apellidos completos'}),
            'idTipoDoc':forms.Select(attrs={'class': 'form-control', 'required': 'required'}),
            'documento':forms.TextInput(attrs={'class': 'form-control', 'required': 'required','placeholder':'Número de documento'}),
            'LugarResidencia':forms.Select(attrs={'class': 'form-control', 'required': 'required'}),
            'fechanacimiento':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'required': 'required','placeholder':'Dia/Mes/Año'}),
            'email':forms.TextInput(attrs={'class': 'form-control', 'required': 'required','placeholder':'Correo electronico'}),
            'telefono':forms.TextInput(attrs={'class': 'form-control', 'required': 'required','placeholder':'Número telefonico'}),
            'usuario':forms.TextInput(attrs={'class': 'form-control', 'required': 'required','placeholder':'Nombre de usuario'}),
            'password':forms.PasswordInput(attrs={'class': 'form-control', 'required': 'required','placeholder':'Contraseña'}),
        }
