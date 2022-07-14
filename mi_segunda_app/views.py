from django.shortcuts import render
from django.http import HttpResponse

def mostrar_autos(request):
    return render(request, "mi_segunda_app/autos.html", {}) 
    
def mostrar_base(request):
    return render(request, "mi_segunda_app/base.html", {}) 