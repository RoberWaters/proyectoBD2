from django.shortcuts import render
from django.db import connections

# Create your views here.

#Pagina Principal
def pagina_principal(request):
    return render(request, 'bitacora/pagina_principal.html')


#BITACORA
def lista_bitacora(request):
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT idBitacora, accion, relacion, fecha, idUsuario, nombreUsuario FROM dbo.BITACORA")
        columnas = [col[0] for col in cursor.description]
        resultados = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    
    # Verifica los resultados
    print(resultados)  # Agrega esto para depuración
    
    return render(request, 'bitacora/lista_bitacora.html', {'bitacoras': resultados})

#Concecionarios
def lista_concesionarios(request):
    with connections['default'].cursor() as cursor:
        # Consulta a la tabla dbo.CONCESIONARIOS
        cursor.execute("SELECT idConcesionario, nombre, direccion, noTelefono FROM dbo.CONCESIONARIOS")
        columnas = [col[0] for col in cursor.description]  # Nombres de las columnas
        resultados = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]  # Combina columnas con datos
    
    # Renderiza la plantilla HTML con los resultados
    return render(request, 'bitacora/lista_concesionarios.html', {'concesionarios': resultados})