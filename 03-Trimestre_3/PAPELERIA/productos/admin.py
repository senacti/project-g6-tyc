from django.contrib import admin

from .models import Producto


class ProductoAdmin(admin.ModelAdmin):
    fields = ('titulo', 'descripcion', 'precio', 'image')
    list_display = ('__str__', 'slug', 'created_at')
admin.site.register(Producto, ProductoAdmin)