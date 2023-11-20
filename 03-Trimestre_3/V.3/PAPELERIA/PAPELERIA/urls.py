
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import login
from django.contrib.auth import logout



urlpatterns = [

#Web Inicio

    path('admin/', admin.site.urls),
    path('',views.MarketplaceIndex,name = 'MarketplaceIndex'),


#Web Cerrada

    #ADMIN

    path('Menu_PrincipalAdmin/',views.Menu_PrincipalAdmin,name = 'Menu_PrincipalAdmin'),

        #PERSONAL

    path('PersonalAdmin/',views.PersonalAdmin,name = 'PersonalAdmin'),
    path('Personal/Administrar_Personal/',views.Administrar_Personal,name = 'Administrar_Personal'),

        #INVENTARIO

    path('InventarioAdmin/',views.InventarioAdmin,name = 'InventarioAdmin'),

        #CAJA

    path('CajaAdmin/',views.CajaAdmin,name = 'CajaAdmin'),

        #PROVEEDORES
    
    path('ProveedoresAdmin/',views.ProveedoresAdmin,name = 'ProveedoresAdmin'),

        #SOCIAL
        
    path('ModulosIndexAdmin/',views.ModulosIndexAdmin,name = 'ModulosIndexAdmin'),



    #EMPLEADO

    path('Menu_Principal/',views.Menu_Principal,name = 'Menu_Principal'),

        #PERSONAL

    path('PersonalEmpleado/',views.PersonalEmpleado,name = 'PersonalEmpleado'),
    path('PersonalEmpleado/Consultar_Personal/',views.Consultar_Personal,name = 'Consultar_Personal'),

        #INVENTARIO

    path('Inventario/',views.Inventario,name = 'Inventario'),
    path('Inventario/Modificar_Inventario',views.Modificar_Inventario,name = 'Modificar_Inventario'),

        #CAJA

    path('Caja/',views.Caja,name = 'Caja'),
    path('Caja/Factura',views.Factura,name = 'Factura'),

        #PROVEEDORES

    path('Proveedores/',views.Proveedores,name = 'Proveedores'),
    path('Proveedores/Modificar_Proveedores/',views.Modificar_Proveedores,name = 'Modificar_Proveedores'),
    path('Proveedores/Devolucion_Proveedores/',views.Devolucion_Proveedores,name = 'Devolucion_Proveedores'),

        #SOCIAL

    path('ModulosIndex/',views.ModulosIndex,name = 'ModulosIndex'),
    path('Ayuda/',views.Ayuda,name = 'Ayuda'),

#Logins, Logouts, Autentificadores, Etc

    path('Login/',views.Login,name = 'Login'),
    path('logout/', views.logout, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('LoginClientes/', views.LoginClientes, name = 'LoginClientes')


# WEB ABIERTA




    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
