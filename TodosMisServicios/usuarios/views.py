from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Usuario,Servicio,Usuario_Servicio

# Create your views here.

def index(request):
	datos = Usuario_Servicio.objects.all()
	dicc = {}
	for dato in datos:
		dicc[dato.usuario]=[]
	for dato in datos:
		dicc[dato.usuario]+=[dato.servicio]
	return render(request,'usuarios/index.html',{'datos':dicc})
