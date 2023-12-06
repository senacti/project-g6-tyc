from django.contrib import admin

from django.urls import path
from django.urls import include

from django.conf.urls.static import static
from django.conf import settings


from . import views

from productos.views import ProductoListView
from categorias.views import CategoriaListView
from productos import views as productos_views
from promo_codes import views as promo_views
from . import views as categorias_views

urlpatterns = [
    path('', ProductoListView.as_view(), name='index'),
    path('usuarios/login', views.login_view, name='login'),
    path('usuarios/logout', views.logout_view, name='logout'),
    path('usuarios/registro', views.register, name='register'),
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),
    path('categorias/', include('categorias.urls')),
    path('carrito/', include('carts.urls')),
    path('orden/', include('orders.urls')),
    path('direcciones/', include('shipping_addresses.urls')),
    path('codigos/', include('promo_codes.urls')),
    path('pagos/', include('billing_profiles.urls')),
    #Web Cerrada
    path('Cerrada/', views.menu_principalEmpleados, name='menu_empleados'),
    path('Cerrada/ProductosEmpleado', productos_views.ProductosListView.as_view(), name='productos_E'),
    path('Cerrada/CategoriasEmpleado', CategoriaListView.as_view(), name='categorias_E'),  
    path('Cerrada/PromocionesEmpleado', promo_views.PromoCodeListView.as_view(), name='promocional_E'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)