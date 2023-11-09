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


#SolicitudPedido, Caja, Inventario, Factura,
    



class SolicitudPedido(models.Model):
    id_producto = models.IntegerField(unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id_producto)


class Caja(models.Model):
    productos = models.ManyToManyField(SolicitudPedido)
    cantidad_caja = models.IntegerField(verbose_name="cantidad")

    def __str__(self):
        return f"Caja {self.id}"


class Inventario(models.Model):
    id_categorias = models.IntegerField()
    id_producto = models.ForeignKey(SolicitudPedido, on_delete=models.PROTECT)
    nombre_categoria = models.CharField(max_length=50, verbose_name="categoria")
    descripcion_categoria = models.TextField(max_length=200, verbose_name="descripcion")
    cantidad = models.IntegerField()
    caja = models.ForeignKey(Caja, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre_categoria} - {self.id_producto}"


class Factura(models.Model):
    caja = models.ForeignKey(Caja, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        # Inicializar el total de la factura
        self.total = sum(
            producto.precio * self.caja.cantidad_caja for producto in self.caja.productos.all()
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Factura {self.id} - Total: {self.total}"



