# Generated by Django 4.0.6 on 2022-08-24 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0017_orden_tiempoentrega'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='emailEntrega',
            field=models.EmailField(default='default@default.com', max_length=254),
        ),
    ]
