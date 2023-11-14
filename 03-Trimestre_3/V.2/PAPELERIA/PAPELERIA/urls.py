
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import login
from django.contrib.auth import logout



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Login,name = 'Login'),
    path('logout/', views.logout, name='logout'),
    
    path('Inventario/',views.Inventario,name = 'Inventario'),

    path('Caja/',views.Caja,name = 'Caja'),

    path('Personal/',views.Personal,name = 'Personal'),
    path('Personal/Administrar_Personal/',views.Administrar_Personal,name = 'Administrar_Personal'),
    path('Personal/Consultar_Personal/',views.Consultar_Personal,name = 'Consultar_Personal'),

    path('Proveedores/',views.Proveedores,name = 'Proveedores'),
    path('Proveedores/Modificar_Proveedores/',views.Modificar_Proveedores,name = 'Modificar_Proveedores'),
    path('Proveedores/Devolucion_Proveedores/',views.Devolucion_Proveedores,name = 'Devolucion_Proveedores'),

    path('ModulosIndex/',views.ModulosIndex,name = 'ModulosIndex'),

    path('Menu_Principal/',views.Menu_Principal,name = 'Menu_Principal'),

    path('Ayuda/',views.Ayuda,name = 'Ayuda')
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
