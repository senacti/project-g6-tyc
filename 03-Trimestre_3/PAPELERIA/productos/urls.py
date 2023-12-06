from django.urls import path

from . import views

app_name = 'productos'

urlpatterns = [
    path('search', views.ProductoSearchListView.as_view(), name='search'),
    path('<slug:slug>', views.ProductoDetailView.as_view(), name='producto' ),
    path('', views.ProductosListView.as_view(), name='lista_productos'),
    path('crear/', views.ProductoCreateView.as_view(), name='crear_producto'),
    path('<int:pk>/actualizar/', views.ProductoUpdateView.as_view(), name='actualizar_producto'),
    path('<int:pk>/eliminar/', views.ProductoDeleteView.as_view(), name='eliminar_producto'),
    
]