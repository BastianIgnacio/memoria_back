# Generated by Django 4.0.6 on 2022-07-10 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocalComercial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.TextField()),
                ('link', models.CharField(max_length=255)),
                ('horarioAtencion', models.TextField()),
                ('tieneDelivery', models.BooleanField(default=False)),
                ('estado', models.CharField(max_length=20)),
                ('privateKeyMercadopago', models.CharField(max_length=25)),
                ('publicKeyMercadopago', models.CharField(max_length=25)),
                ('tieneMercadopago', models.BooleanField(default=False)),
            ],
        ),
    ]
