from django.shortcuts import render
from django.db import connections
from django.http import JsonResponse

# Create your views here.

def lista_clientes(request):
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT * FROM dbo.CLIENTES")
        columnas = [col[0] for col in cursor.description]  # Obtén los nombres de las columnas
        resultados = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]  # Combina columnas con datos
    
    return JsonResponse(resultados, safe=False)


