from django.urls import path

from . import views

from .decorators import empleado_required

app_name = 'codigos_promocion'

urlpatterns = [
    path('validar', views.validate, name='validate'),
    path('', empleado_required(views.PromoCodeListView.as_view()), name='lista_promociones'),
    path('crear/', empleado_required(views.PromoCodeCreateView.as_view()), name='crear_promocion'),
    path('<int:pk>/actualizar/', empleado_required(views.PromoCodeUpdateView.as_view()), name='actualizar_promocion'),
    path('<int:pk>/eliminar/', empleado_required(views.PromoCodeDeleteView.as_view()), name='eliminar_promocion'),
    
]