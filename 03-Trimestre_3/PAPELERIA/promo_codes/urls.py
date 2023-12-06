from django.urls import path

from . import views

app_name = 'promo_codes'

urlpatterns = [
    path('validar', views.validate, name='validate'),
    path('', views.PromoCodeListView.as_view(), name='lista_promociones'),
    path('crear/', views.PromoCodeCreateView.as_view(), name='crear_promocion'),
    path('<int:pk>/actualizar/', views.PromoCodeUpdateView.as_view(), name='actualizar_promocion'),
    path('<int:pk>/eliminar/', views.PromoCodeDeleteView.as_view(), name='eliminar_promocion'),
    
]