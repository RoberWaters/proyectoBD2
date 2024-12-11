from django.shortcuts import render
from django.db import connections

# Create your views here.

#BITACORA
def lista_bitacora(request):
    with connections['default'].cursor() as cursor:
        # Consulta a la tabla dbo.BITACORA
        cursor.execute("SELECT idBitacora, accion, relacion, fecha, idUsuario, nombreUsuario FROM dbo.BITACORA")
        columnas = [col[0] for col in cursor.description]  # Nombres de las columnas
        resultados = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]  # Combina columnas con datos
    
    # Renderiza la plantilla HTML con los resultados
    return render(request, 'bitacora/lista_bitacora.html', {'bitacora': resultados})