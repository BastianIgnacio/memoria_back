# Generated by Django 4.0.6 on 2022-09-26 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0024_localcomercial_telefono_alter_venta_estadoventa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localcomercial',
            name='telefono',
            field=models.CharField(default='+569XXXXXXX', max_length=12),
        ),
    ]
