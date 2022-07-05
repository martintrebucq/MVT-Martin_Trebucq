from django.shortcuts import render
from django.http import HttpResponse

def familia(request):
    context = {}
    return render(request,'mi_primer_app/index.html',context)

