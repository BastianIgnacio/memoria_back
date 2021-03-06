# Generated by Django 4.0.6 on 2022-07-12 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0007_orden_productoorden'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='refLocalComercial',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='baseApp.localcomercial'),
        ),
        migrations.AddField(
            model_name='orden',
            name='refVenta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='baseApp.venta'),
        ),
        migrations.AddField(
            model_name='productoorden',
            name='refOrden',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='baseApp.orden'),
        ),
    ]
