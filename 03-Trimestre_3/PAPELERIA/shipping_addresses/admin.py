from django.contrib import admin
from .models import ShippingAddress

class ShippingAddressAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dirección', {
            'fields': ('user', 'line1', 'line2', 'line3', 'department', 'street_type', 'reference', 'postal_code')
        }),
        ('Detalles', {
            'fields': ('is_home_or_work', 'contact_phone', 'default')
        }),
        ('Información adicional', {
            'fields': ('get_address',),  # Campo de dirección
            'classes': ('collapse',),  # Opcional: colapsar este campo por defecto
        }),
    )

    readonly_fields = ('get_address',)  # Hacer el campo de dirección de solo lectura

    list_display = ('user', 'line1', 'department', 'default', 'address')
    list_filter = ('is_home_or_work', 'default')

    def get_address(self, obj):
        return obj.address

    get_address.short_description = 'Address'

admin.site.register(ShippingAddress, ShippingAddressAdmin)