from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from mi_primera_app.models import Automoviles, Familia ,Longevidad_animales

def familia(request):
    context = {}
    return render(request,'mi_primer_app/index.html',context)

def datos_familiares(request):
    context = {}
    context['familia'] = Familia.objects.all()
    return render(request,'mi_primer_app/datos-familia.html',context)

def modelo_autos (request):
    context = {}
    context['autos'] = Automoviles.objects.all()
    return render(request,'mi_primer_app/autos.html',context )