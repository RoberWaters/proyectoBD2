from django.shortcuts import render
from django.db import connections
from django.http import JsonResponse

# Create your views here.

def lista_clientes(request):
    with connections['default'].cursor() as cursor:
        # Consulta a la tabla dbo.CLIENTES
        cursor.execute("SELECT idCliente, nombre, direccion, noTelefono, sexo, ingresosAnuales FROM dbo.CLIENTES")
        columnas = [col[0] for col in cursor.description]  # Nombres de las columnas
        resultados = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]  # Combina columnas con datos
    
    # Renderiza la plantilla HTML con los resultados
    return render(request, 'clientes/lista_clientes.html', {'clientes': resultados})

