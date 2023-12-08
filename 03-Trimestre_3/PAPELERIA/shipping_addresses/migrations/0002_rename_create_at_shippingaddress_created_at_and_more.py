# Generated by Django 4.2.7 on 2023-12-07 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_addresses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='contact_phone',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='department',
            field=models.CharField(choices=[('amazonas', 'Amazonas'), ('antioquia', 'Antioquia'), ('arauca', 'Arauca'), ('atlantico', 'Atlántico'), ('bolivar', 'Bolívar'), ('boyaca', 'Boyacá'), ('caldas', 'Caldas'), ('caqueta', 'Caquetá'), ('casanare', 'Casanare'), ('cauca', 'Cauca'), ('cesar', 'Cesar'), ('choco', 'Chocó'), ('cordoba', 'Córdoba'), ('cundinamarca', 'Cundinamarca'), ('guainia', 'Guainía'), ('guaviare', 'Guaviare'), ('huila', 'Huila'), ('guajira', 'La Guajira'), ('magdalena', 'Magdalena'), ('meta', 'Meta'), ('narino', 'Nariño'), ('norte_santander', 'Norte de Santander'), ('putumayo', 'Putumayo'), ('quindio', 'Quindío'), ('risaralda', 'Risaralda'), ('san_andres', 'San Andrés y Providencia'), ('santander', 'Santander'), ('sucre', 'Sucre'), ('tolima', 'Tolima'), ('valle_cauca', 'Valle del Cauca'), ('vaupes', 'Vaupés'), ('vichada', 'Vichada')], default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='is_home_or_work',
            field=models.CharField(choices=[('home', 'Casa'), ('work', 'Trabajo')], default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='line3',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='street_type',
            field=models.CharField(choices=[('avenida', 'Avenida'), ('avenida_calle', 'Avenida Calle'), ('avenida_carrera', 'Avenida Carrera'), ('calle', 'Calle'), ('carrera', 'Carrera'), ('circular', 'Circular'), ('circunvalar', 'Circunvalar'), ('diagonal', 'Diagonal'), ('manzana', 'Manzana'), ('transversal', 'Transversal'), ('via', 'Vía')], default='', max_length=50),
            preserve_default=False,
        ),
    ]
