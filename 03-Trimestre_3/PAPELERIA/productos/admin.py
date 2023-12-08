from django.contrib import admin
from django.utils.html import format_html
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    fields = ('titulo', 'descripcion', 'precio', 'image')
    list_display = ('__str__', 'slug', 'created_at', 'imagen')
    readonly_fields = ('imagen',)

    def imagen(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50"/>'.format(obj.image.url))
        else:
            return '(No imagen)'

    imagen.allow_tags = True
    imagen.short_description = 'Imagen'

admin.site.register(Producto, ProductoAdmin)