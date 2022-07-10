# Generated by Django 4.0.6 on 2022-07-10 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0002_venta'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('precioUnitario', models.IntegerField()),
                ('nombreProducto', models.CharField(max_length=255)),
                ('descripcionProducto', models.TextField()),
                ('notaEspecial', models.TextField()),
            ],
        ),
    ]
