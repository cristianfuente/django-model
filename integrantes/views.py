from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Ciudad
from .models import TipoDocumento
from .models import Persona
from django.http import HttpResponseRedirect
from .forms import RegistroForm

def integrantes(request):
    personas=Persona.objects.all()
    template=loader.get_template('integrantes/integrantes.html')
    context={
        'personas':personas,
        }
    return HttpResponse(template.render(context,request))

def home(request):
    template=loader.get_template('index.html')
    context={}
    return HttpResponse(template.render(context,request))

def success(request):
    template=loader.get_template('integrantes/success.html')
    context={}
    return HttpResponse(template.render(context,request))

def prueba(request):
    template=loader.get_template('integrantes/prueba.html')
    context={}
    return HttpResponse(template.render(context,request))

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            nombres1=form.cleaned_data['nombres']
            apellidos1=form.cleaned_data['apellidos']
            idTipoDoc1=form.cleaned_data['idTipoDoc']
            documento1=form.cleaned_data['documento']
            LugarResidencia1=form.cleaned_data['LugarResidencia']
            fechanacimiento1=form.cleaned_data['fechanacimiento']
            email1=form.cleaned_data['email']
            telefono1=form.cleaned_data['telefono']
            usuario1=form.cleaned_data['usuario']
            password1=form.cleaned_data['password']
            persona1=Persona(
                nombres = nombres1,
                apellidos = apellidos1,
                idTipoDoc = idTipoDoc1,
                documento=documento1,
                LugarResidencia= LugarResidencia1,
                fechanacimiento=fechanacimiento1,
                email=email1,
                telefono=telefono1,
                usuario=usuario1,
                password=password1
            )
            persona1.save()
            return redirect('../success')
    else:
        form= RegistroForm()
    return render(request,'integrantes/registro.html',{'form':form})
