from django.shortcuts import render, redirect
from django.db import connections
from .models import Usuario


# Create your views here.

#Pagina Principal
def pagina_principal(request):
    return render(request, 'vistas/pagina_principal.html')


#CLIENTES
def lista_clientes(request):
    with connections['default'].cursor() as cursor:
        # Consulta a la tabla dbo.CLIENTES
        cursor.execute("SELECT idCliente, nombre, direccion, noTelefono, sexo, ingresosAnuales FROM dbo.CLIENTES")
        columnas = [col[0] for col in cursor.description]  # Nombres de las columnas
        resultados = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]  # Combina columnas con datos
    
    # Renderiza la plantilla HTML con los resultados
    return render(request, 'vistas/lista_clientes.html', {'clientes': resultados})



#BITACORA
def lista_bitacora(request):
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT idBitacora, accion, relacion, fecha, idUsuario, nombreUsuario FROM dbo.BITACORA")
        columnas = [col[0] for col in cursor.description]
        resultados = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    
    # Verifica los resultados
    print(resultados)  # Agrega esto para depuración
    
    return render(request, 'vistas/lista_bitacora.html', {'bitacoras': resultados})

#Concecionarios
def lista_concesionarios(request):
    with connections['default'].cursor() as cursor:
        # Consulta a la tabla dbo.CONCESIONARIOS
        cursor.execute("SELECT idConcesionario, nombre, direccion, noTelefono FROM dbo.CONCESIONARIOS")
        columnas = [col[0] for col in cursor.description]  # Nombres de las columnas
        resultados = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]  # Combina columnas con datos
    
    # Renderiza la plantilla HTML con los resultados
    return render(request, 'vistas/lista_concesionarios.html', {'concesionarios': resultados})

#VEHICULOS
def lista_vehiculos(request):
    with connections['default'].cursor() as cursor:
        # Consulta a la tabla dbo.VEHICULOS
        cursor.execute("SELECT VIN, idModelo, color, noMotor, transmision FROM dbo.VEHICULOS")
        columnas = [col[0] for col in cursor.description]  # Nombres de las columnas
        resultados = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]  # Combina columnas con datos
    
    # Renderiza la plantilla HTML con los resultados
    return render(request, 'vistas/lista_vehiculos.html', {'vehiculos': resultados})

#PROVEEDORES
def lista_proveedores(request):
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT idProveedor, nombre, direccion, noTelefono FROM dbo.PROVEEDORES")
        columnas = [col[0] for col in cursor.description]
        resultados = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    
    return render(request, 'vistas/lista_proveedores.html', {'proveedores': resultados})

#MODELOS
def lista_modelos(request):
    with connections['default'].cursor() as cursor:
        # Consulta a la tabla dbo.MODELOS
        cursor.execute("SELECT idModelo, nombre, estiloCarroceria, marca FROM dbo.MODELOS")
        columnas = [col[0] for col in cursor.description]  # Nombres de las columnas
        resultados = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]  # Combina columnas con datos
    
    # Renderiza la plantilla HTML con los resultados
    return render(request, 'vistas/lista_modelos.html', {'modelos': resultados})

#PLANTAS
def lista_plantas(request):
    with connections['default'].cursor() as cursor:
        # Consulta a la tabla dbo.PLANTAS
        cursor.execute("SELECT idPlanta, nombre, ubicacion FROM dbo.PLANTAS")
        columnas = [col[0] for col in cursor.description]  # Nombres de las columnas
        resultados = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]  # Combina columnas con datos
    
    # Renderiza la plantilla HTML con los resultados
    return render(request, 'vistas/lista_plantas.html', {'plantas': resultados})


#VENTAS
def lista_ventas(request):
    with connections['default'].cursor() as cursor:
        # Consulta a la tabla dbo.VENTAS
        cursor.execute("SELECT idVenta, fecha, idConcesionario, idCliente, VIN, precio FROM dbo.VENTAS")
        columnas = [col[0] for col in cursor.description]  # Nombres de las columnas
        resultados = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]  # Combina columnas con datos
    
    # Renderiza la plantilla HTML con los resultados
    return render(request, 'vistas/lista_ventas.html', {'ventas': resultados})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            # Busca al usuario en la base de datos
            usuario = Usuario.objects.get(username=username, password=password)

            # Redirige según el rol
            if usuario.role == "Administrador":
                return redirect("pagina_principal")  # Redirige a la página principal
            elif usuario.role == "Marketing":
                return redirect("pagina_marketing")  # Página de marketing
            elif usuario.role == "Cliente":
                return redirect("pagina_cliente")  # Página del cliente

        except Usuario.DoesNotExist:
            # Si el usuario no existe o la contraseña es incorrecta
            return render(request, "vistas/login.html", {"error": "Usuario o contraseña incorrectos."})

    # Si no es POST, simplemente renderiza el formulario de login
    return render(request, "vistas/login.html")



def pagina_marketing(request):
    return render(request, "vistas/pagina_marketing.html")

def pagina_cliente(request):
    return render(request, "vistas/pagina_cliente.html")

#ENUM_COLOR
def lista_colores(request):
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT color FROM dbo.ENUM_COLOR")
        columnas = [col[0] for col in cursor.description]
        resultados = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    
    # Verifica los resultados
    print(resultados)  # Agrega esto para depuración
    
    return render(request, 'vistas/lista_colores.html', {'colores': resultados})

#ENUM_MARCAS
def lista_marcas(request):
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT marca FROM dbo.ENUM_MARCAS")
        columnas = [col[0] for col in cursor.description]
        resultados = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    
    # Verifica los resultados
    print(resultados)  # Agrega esto para depuración
    
    return render(request, 'vistas/lista_marcas.html', {'marcas': resultados})

#ENUM TRANSMISION
def lista_transmision(request):
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT transmision FROM dbo.ENUM_TRANSMISION")
        columnas = [col[0] for col in cursor.description]
        resultados = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    
    # Verifica los resultados
    print(resultados)  # Agrega esto para depuración
    
    return render(request, 'vistas/lista_transmision.html', {'transmisiones': resultados})


#MODELOSXPLANTAS
def lista_modelosxplantas(request):
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT idModelo, idPlanta
            FROM dbo.MODELOSXPLANTAS
        """)
        columnas = [col[0] for col in cursor.description]
        resultados = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    
    # Verifica los resultados
    print(resultados)  # Agrega esto para depuración
    
    return render(request, 'vistas/lista_modelosxplantas.html', {'modelosxplantas': resultados})