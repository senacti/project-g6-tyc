from django.db import models
from productos.models import Producto

class Categoria(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    productos = models.ManyToManyField(Producto, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.titulo