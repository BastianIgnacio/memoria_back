# Generated by Django 4.0.6 on 2022-09-21 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0023_localcomercial_comuna_localcomercial_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='localcomercial',
            name='telefono',
            field=models.CharField(default='+569XXXXXXX', max_length=11),
        ),
        migrations.AlterField(
            model_name='venta',
            name='estadoVenta',
            field=models.CharField(default='EN_PROCESO', max_length=50),
        ),
    ]
