"""
URL configuration for myBD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

#Trayendo vistas de las apps
from clientes.views import lista_clientes  
from bitacora.views import lista_bitacora, pagina_principal, lista_concesionarios, lista_vehiculos,lista_proveedores, lista_modelos, lista_plantas, lista_ventas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pagina_principal, name='pagina_principal'),  # Página principal
    path('clientes/', lista_clientes, name='lista_clientes'),  # Define la URL para clientes
    path('bitacoras/', lista_bitacora, name='lista_bitacora'), #URL para bitacoras
    path('concesionarios/', lista_concesionarios, name='lista_concesionarios'),
    path('vehiculos/', lista_vehiculos, name='lista_vehiculos'),
    path('proveedores/', lista_proveedores, name='lista_proveedores'),
    path('modelos/', lista_modelos, name='lista_modelos'),
    path('plantas/', lista_plantas, name='lista_plantas'),
    path('ventas/', lista_ventas, name='lista_ventas'),
]

