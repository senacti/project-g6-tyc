from django.urls import path
from . import views
from .decorators import empleado_required

app_name = 'categorias'


urlpatterns = [
    path('', empleado_required(views.CategoriaListView.as_view()), name='lista_categorias'),
    path('crear/', empleado_required(views.CategoriaCreateView.as_view()), name='crear_categoria'),
    path('<int:pk>/actualizar/', empleado_required(views.CategoriaUpdateView.as_view()), name='actualizar_categoria'),
    path('<int:pk>/eliminar/', empleado_required(views.CategoriaDeleteView.as_view()), name='eliminar_categoria'),
]
