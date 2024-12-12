from django.shortcuts import render, redirect
from .models import Usuario

from django.shortcuts import render, redirect
from vistas.models import Usuario  # Asegúrate de importar el modelo desde la app vistas si lo migras allí.

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            usuario = Usuario.objects.get(username=username, password=password)

            # Redirigir según el rol
            if usuario.role == "Administrador":
                return redirect("pagina_principal")  # Redirige a la página principal en vistas/views.py
            elif usuario.role == "Marketing":
                return redirect("pagina_marketing")  # Página marketing en vistas/views.py
            elif usuario.role == "Cliente":
                return redirect("pagina_cliente")  # Página cliente en vistas/views.py
        except Usuario.DoesNotExist:
            return render(request, "autenticacion/login.html", {"error": "Usuario o contraseña incorrectos."})

    return render(request, "autenticacion/login.html")


def pagina_principal(request):
    return render(request, "autenticacion/pagina_principal.html")

def pagina_marketing(request):
    return render(request, "autenticacion/pagina_marketing.html")  # Cambié la plantilla a pagina_marketing.html

def pagina_cliente(request):
    return render(request, "autenticacion/pagina_cliente.html")  # Cambié la plantilla a pagina_cliente.html
