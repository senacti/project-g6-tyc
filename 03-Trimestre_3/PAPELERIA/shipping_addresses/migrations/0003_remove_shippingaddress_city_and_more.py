# Generated by Django 4.2.7 on 2023-12-07 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_addresses', '0002_rename_create_at_shippingaddress_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='city',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='country',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='state',
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='department',
            field=models.CharField(choices=[('amazonas', 'Amazonas'), ('antioquia', 'Antioquia'), ('arauca', 'Arauca'), ('atlantico', 'Atlántico'), ('bolivar', 'Bolívar'), ('boyaca', 'Boyacá'), ('bogotá D.C', 'Bogotá D.C'), ('caldas', 'Caldas'), ('caqueta', 'Caquetá'), ('casanare', 'Casanare'), ('cauca', 'Cauca'), ('cesar', 'Cesar'), ('choco', 'Chocó'), ('cordoba', 'Córdoba'), ('cundinamarca', 'Cundinamarca'), ('guainia', 'Guainía'), ('guaviare', 'Guaviare'), ('huila', 'Huila'), ('guajira', 'La Guajira'), ('magdalena', 'Magdalena'), ('meta', 'Meta'), ('narino', 'Nariño'), ('norte_santander', 'Norte de Santander'), ('putumayo', 'Putumayo'), ('quindio', 'Quindío'), ('risaralda', 'Risaralda'), ('san_andres', 'San Andrés y Providencia'), ('santander', 'Santander'), ('sucre', 'Sucre'), ('tolima', 'Tolima'), ('valle_cauca', 'Valle del Cauca'), ('vaupes', 'Vaupés'), ('vichada', 'Vichada')], max_length=100),
        ),
    ]