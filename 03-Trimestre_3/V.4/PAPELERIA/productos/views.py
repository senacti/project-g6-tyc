from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

from django.db.models import Q

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Producto

class ProductoListView(ListView):
    template_name = 'index.html'
    queryset = Producto.objects.all().order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de productos'
        context['productos'] = context['producto_list']

        return context

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'productos/producto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        print(context)

        return context
    
class ProductoSearchListView(ListView):
    template_name = 'productos/search.html'
    
    def get_queryset(self):
        filters = Q(titulo__icontains=self.query()) | Q(categoria__titulo__icontains=self.query())

        #SELECT * FROM productos WHERE title like %valor% 
        return Producto.objects.filter(filters)
    
    def query(self):
        return self.request.GET.get('q')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] = context['producto_list'].count()


        return context