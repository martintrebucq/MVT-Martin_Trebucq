"""mi_primer_proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mi_primera_app.views import familia
from mi_primera_app.views import datos_familiares
from mi_primera_app.views import modelo_autos
from mi_segunda_app.views import mostrar_autos, mostrar_base
from mi_segunda_app.views import mostrar_autos
urlpatterns = [
    path('admin/', admin.site.urls),
    path('familia/',familia),
    path('datos-familiares',datos_familiares),
    path('autos',modelo_autos),
    path('mostrar-autos',mostrar_autos),
    path('mostrar-base',mostrar_base),
    
]
