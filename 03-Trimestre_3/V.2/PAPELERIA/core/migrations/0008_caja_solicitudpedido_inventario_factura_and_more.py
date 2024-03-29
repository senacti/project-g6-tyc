# Generated by Django 4.2.7 on 2023-11-09 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_informacion_personal_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_caja', models.IntegerField(verbose_name='cantidad')),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_producto', models.IntegerField(unique=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_categorias', models.IntegerField()),
                ('nombre_categoria', models.CharField(max_length=50, verbose_name='categoria')),
                ('descripcion_categoria', models.TextField(max_length=200, verbose_name='descripcion')),
                ('cantidad', models.IntegerField()),
                ('caja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.caja')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.solicitudpedido')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('caja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.caja')),
            ],
        ),
        migrations.AddField(
            model_name='caja',
            name='productos',
            field=models.ManyToManyField(to='core.solicitudpedido'),
        ),
    ]
