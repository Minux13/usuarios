from django.shortcuts import render

from django.http import HttpResponse
from .forms import RegistroFormulario
from .models import Usuarios_registrado
#import datetime

def index(request):
    formulario = RegistroFormulario(request.POST or None)
    context = {
        "form" : formulario
    }

    #if formulario.is_valid():
    if formulario.is_valid():
        datosFormulario = formulario.cleaned_data
        nombre_ingresado = datosFormulario.get("nombre")
        objeto = Usuarios_registrado.objects.create(nombre=nombre_ingresado)
    #now = datetime.datetime.now()
    #html = "<html><body><h1>It is now </h1></body></html>" % now
    return render(request, 'index.html', context)
    #return HttpResponse(html)
