from django.db import models




class cargo(models.Model):
    cargo = models.CharField(max_length=50, verbose_name="Cargo")

    def __str__(self):
        return self.cargo
    


class informacion_personal(models.Model):
    nombres = models.CharField(max_length=50, verbose_name="Nombres", default="")
    apellidos  = models.CharField(max_length=50, verbose_name="Apellidos")
    correo = models.CharField(max_length=50, verbose_name="Correo")
    telefono = models.CharField(max_length=10, verbose_name="Telefono")
    cargo = models.ForeignKey(cargo, on_delete=models.PROTECT)
    direccion = models.TextField(verbose_name="Direccion")
    salario = models.IntegerField(verbose_name="Salario")
    horas_trabajo= models.TextField(verbose_name="Horas Trabajo")
    inicio_contrato = models.DateField(verbose_name="Inicio contrato")
    imagen = models.ImageField(upload_to="media", null=True)

    def __str__(self):
        return self.nombres

        for field_name, field in self.fields.items():
            field.widget.attrs['autocomplete'] = 'off'

#SolicitudPedido, Caja, Inventario, Factura,
    

class proveedores(models.Model):
    nombre_proveedores = models.CharField(max_length=50, verbose_name="Proveedor:")
    razon_social = models.TextField(verbose_name="Razon social:")
    direccion = models.CharField(max_length=40, verbose_name="Direccion:")
    telefono = models.IntegerField(verbose_name="Telefono:")
    Correo = models.CharField(max_length=40, verbose_name="Correo Electronico:")
    inicio_contrato_proveedores = models.DateField(verbose_name="Inicio contrato")

    def __str__(self):
        return self.nombre_proveedores

class categoria(models.Model):
    nombre_categoria = models.CharField(max_length=50, verbose_name="Categoria:")


    def __str__(self):
        return self.nombre_categoria
    
class Inventario(models.Model):
    nombre_categoria = models.ForeignKey(categoria, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_proveedores = models.ForeignKey(proveedores, on_delete=models.PROTECT)
    descripcion_categoria = models.TextField(max_length=200, verbose_name="Descripcion:")

    def save(self, *args, **kwargs):
        # Verificar si ya existe un inventario con la misma categoría y proveedor, excluyendo el inventario actual
        existing_inventory = Inventario.objects.filter(
            nombre_categoria=self.nombre_categoria,
            nombre_proveedores=self.nombre_proveedores
        ).exclude(pk=self.pk).first()

        if existing_inventory:
            # Si existe, actualizar la cantidad y precio
            existing_inventory.cantidad += self.cantidad
            existing_inventory.precio = self.precio
            existing_inventory.save()
        else:
            # Si no existe, guardar como de costumbre
            super(Inventario, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre_categoria} - {self.nombre_proveedores} - {self.pk}"


class Factura(models.Model):
    Inventario_id = models.ForeignKey(Inventario, on_delete=models.PROTECT, verbose_name="Producto:")
    cantidad = models.IntegerField(verbose_name="Cantidad:")
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    def save(self, *args, **kwargs):
        # Verificar si hay suficiente cantidad en inventario
        if self.cantidad <= self.Inventario_id.cantidad:
            # Restar la cantidad vendida al inventario
            self.Inventario_id.cantidad -= self.cantidad
            self.Inventario_id.save()  # Guardar la actualización del inventario

            # Calcular y guardar el total de la factura
            self.total = self.Inventario_id.precio * self.cantidad

            # Guardar la factura
            super().save(*args, **kwargs)
        else:
            # No hay suficiente cantidad en inventario
            raise ValueError("No hay suficientes productos en inventario")

    def __str__(self):
        return str(self.total)






