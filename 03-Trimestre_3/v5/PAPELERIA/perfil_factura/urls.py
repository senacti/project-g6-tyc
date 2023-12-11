from django.urls import path

from . import views

app_name = 'perfi_factura'

urlpatterns = [
    path('nuevo', views.create, name='create')
]