from django.urls import path

from . import views

from .decorators import empleado_required

app_name = 'productos'

urlpatterns = [
    path('search', views.ProductoSearchListView.as_view(), name='search'),
    path('<slug:slug>', views.ProductoDetailView.as_view(), name='producto' ),
    path('', empleado_required(views.ProductosListView.as_view()), name='lista_productos'),
    path('crear/', empleado_required(views.ProductoCreateView.as_view()), name='crear_producto'),
    path('<int:pk>/actualizar/', empleado_required(views.ProductoUpdateView.as_view()), name='actualizar_producto'),
    path('<int:pk>/eliminar/', empleado_required(views.ProductoDeleteView.as_view()), name='eliminar_producto'),
    
]