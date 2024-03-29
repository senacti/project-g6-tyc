from django.contrib import admin

from django.urls import path
from django.urls import include

from django.conf.urls.static import static
from django.conf import settings


from . import views

from productos.views import ProductoListView
from categorias.views import CategoriaListView
from productos import views as productos_views
from codigos_promocion import views as promo_views
from .decorators import empleado_required

urlpatterns = [
    path('', ProductoListView.as_view(), name='index'),
    path('usuarios/login', views.login_view, name='login'),
    path('usuarios/logout', views.logout_view, name='logout'),
    path('usuarios/registro', views.register, name='register'),
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),
    path('categorias/', include('categorias.urls')),
    path('carrito/', include('carts.urls')),
    path('orden/', include('pedidos.urls')),
    path('direcciones/', include('direccion.urls')),
    path('codigos/', include('codigos_promocion.urls')),
    path('pagos/', include('perfil_factura.urls')),
    #Web Cerrada
    path('Cerrada/', views.menu_principalEmpleados, name='menu_empleados'),
    path('Cerrada/ProductosEmpleado', empleado_required(productos_views.ProductosListView.as_view()), name='productos_E'),
    path('Cerrada/CategoriasEmpleado', empleado_required(CategoriaListView.as_view()), name='categorias_E'),  
    path('Cerrada/PromocionesEmpleado', empleado_required(promo_views.PromoCodeListView.as_view()), name='promocional_E'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)