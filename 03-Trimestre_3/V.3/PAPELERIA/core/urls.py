from django.urls import path
from .autocomplete import CategoriaAutocomplete
from . import views

app_name = 'core'

urlpatterns = [
    # Configuraciones de URL específicas de la aplicación "core"
    path('categoria-autocomplete/', CategoriaAutocomplete.as_view(), name='categoria-autocomplete'),
    # Otras configuraciones de URL de la aplicación "core"
]