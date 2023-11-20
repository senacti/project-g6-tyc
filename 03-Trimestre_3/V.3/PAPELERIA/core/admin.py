from django.contrib import admin
from .models import cargo, informacion_personal,Inventario, Factura, categoria, proveedores
# Register your models here.

@admin.register(informacion_personal)
class InformacionPersonalAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'correo', 'telefono', 'cargo', 'direccion', 'salario', 'inicio_contrato', 'horas_trabajo', 'imagen')
    list_editable = ('salario', 'horas_trabajo')
    search_fields = ('nombres', 'apellidos', 'correo')
    list_filter = ('cargo',)
    list_per_page = 1

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_categoria', 'descripcion_categoria', 'cantidad', 'total', 'fecha_creacion')

    def nombre_categoria(self, obj):
        return obj.Inventario_id.nombre_categoria.nombre_categoria  # Accede al nombre de la categoría a través del ForeignKey

    def descripcion_categoria(self, obj):
        return obj.Inventario_id.descripcion_categoria  # Accede a la descripción de la categoría


admin.site.register(cargo)
admin.site.register(categoria)

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    search_fields = ['nombre_categoria__nombre_categoria']
    list_display = ('nombre_categoria', 'nombre_proveedores', 'descripcion_categoria', 'cantidad', 'precio')
    search_fields = ('nombre_categoria__nombre_categoria', )
    list_filter = ('nombre_categoria__nombre_categoria',)
    ordering = ('nombre_categoria__nombre_categoria', 'cantidad')  # Añadí 'cantidad' para permitir el ordenamiento por esa columna

    class Media:
        js = ('https://code.jquery.com/jquery-3.6.4.min.js',)

    def nombre_categoria(self, obj):
        return obj.nombre_categoria.nombre_categoria

    def descripcion_categoria(self, obj):
        return obj.nombre_categoria.descripcion_categoria

    nombre_categoria.admin_order_field = 'nombre_categoria__nombre_categoria'


@admin.register(proveedores)
class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('nombre_proveedores', 'direccion', 'Correo', 'telefono', 'inicio_contrato_proveedores')





