from django.contrib import admin
from django.urls import path, include
from vistas import views as vistas_views  # Importa vistas desde la app vistas

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Página principal y otras vistas
    path('', vistas_views.login_view, name='login'),
    path('clientes/', vistas_views.lista_clientes, name='lista_clientes'),
    path('bitacoras/', vistas_views.lista_bitacora, name='lista_bitacora'),
    path('concesionarios/', vistas_views.lista_concesionarios, name='lista_concesionarios'),
    path('vehiculos/', vistas_views.lista_vehiculos, name='lista_vehiculos'),
    path('proveedores/', vistas_views.lista_proveedores, name='lista_proveedores'),
    path('modelos/', vistas_views.lista_modelos, name='lista_modelos'),
    path('plantas/', vistas_views.lista_plantas, name='lista_plantas'),
    path('ventas/', vistas_views.lista_ventas, name='lista_ventas'),
    path('colores/', vistas_views.lista_colores, name='lista_colores'),
    path('marcas/', vistas_views.lista_marcas, name='lista_marcas'),
    path('transmision/', vistas_views.lista_transmision, name='lista_transmision'),
    path('modelosxplantas/', vistas_views.lista_modelosxplantas, name='lista_modelosxplantas'),
    path('modelosxproveedores/', vistas_views.lista_modelosxproveedores, name='lista_modelosxproveedores'),
    path('vehiculosxconcesionarios/', vistas_views.lista_vehiculosxconcesionarios, name='lista_vehiculosxconcesionarios'),
    path('dias_en_inventario/', vistas_views.lista_dias_en_inventario, name='lista_dias_en_inventario'),
    path('marcas_mas_caras/', vistas_views.lista_marcas_mas_caras, name='lista_marcas_mas_caras'),
    path('marcas_mas_vendidas/', vistas_views.lista_marcas_mas_vendidas, name='lista_marcas_mas_vendidas'),
    path('meses_para_convertibles/', vistas_views.lista_meses_para_convertibles, name='lista_meses_para_convertibles'),
    path('proveedores_en_rango/', vistas_views.lista_proveedores_en_rango, name='lista_proveedores_en_rango'),
    path('tendencias/', vistas_views.lista_tendencias, name='lista_tendencias'),
    path('vehiculos_en_inventario/', vistas_views.lista_vehiculos_en_inventario, name='lista_vehiculos_en_inventario'),

    # Rutas de autenticación ahora dentro de vistas
    path('login/', vistas_views.login_view, name='login'),  # Login en vistas
    path('pagina_principal/', vistas_views.pagina_principal, name='pagina_principal'),
    path('pagina_marketing/', vistas_views.pagina_marketing, name='pagina_marketing'),
    path('pagina_cliente/', vistas_views.pagina_cliente, name='pagina_cliente'),
]
