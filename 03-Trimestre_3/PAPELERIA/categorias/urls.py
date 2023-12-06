from django.urls import path
from . import views

app_name = 'categorias'

urlpatterns = [
    path('', views.CategoriaListView.as_view(), name='lista_categorias'),
    path('crear/', views.CategoriaCreateView.as_view(), name='crear_categoria'),
    path('<int:pk>/actualizar/', views.CategoriaUpdateView.as_view(), name='actualizar_categoria'),
    path('<int:pk>/eliminar/', views.CategoriaDeleteView.as_view(), name='eliminar_categoria'),
]
