from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Categoria

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'web_cerrada/categorias/lista_categorias.html'
    context_object_name = 'categorias'

class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ['titulo', 'descripcion', 'productos']
    template_name = 'web_cerrada/categorias/crear_categoria.html'
    success_url = reverse_lazy('categorias:lista_categorias')

class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = ['titulo', 'descripcion', 'productos']
    template_name = 'web_cerrada/categorias/actualizar_categoria.html'
    success_url = reverse_lazy('categorias:lista_categorias')

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'web_cerrada/categorias/eliminar_categoria.html'
    success_url = reverse_lazy('categorias:lista_categorias')
