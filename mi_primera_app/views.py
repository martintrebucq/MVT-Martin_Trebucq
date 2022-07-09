from django.shortcuts import render
from django.http import HttpResponse
from mi_primera_app.models import Familia

def familia(request):
    context = {}
    return render(request,'mi_primer_app/index.html',context)

def datos_familiares(request):
    context = {}
    context['familia'] = Familia.objects.all()
    return render(request,'mi_primer_app/datos-familia.html',context)

