# Generated by Django 4.2.7 on 2023-11-30 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_producto_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='image',
            field=models.ImageField(default='', upload_to='productos/'),
            preserve_default=False,
        ),
    ]
