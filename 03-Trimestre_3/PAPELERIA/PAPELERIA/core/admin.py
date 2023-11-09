from django.contrib import admin
from .models import cargo, informacion_personal, SolicitudPedido, Caja, Inventario, Factura 
# Register your models here.

@admin.register(informacion_personal)
class InformacionPersonalAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'correo', 'telefono', 'cargo', 'direccion', 'salario', 'horas_trabajo', 'inicio_contrato', 'imagen')
    list_editable = ('salario', 'horas_trabajo')
    search_fields = ('nombres', 'apellidos', 'correo')
    list_filter = ('cargo',)
    list_per_page = 1
admin.site.register(cargo)

admin.site.register(SolicitudPedido)
admin.site.register(Caja)
admin.site.register(Inventario)
admin.site.register(Factura)


