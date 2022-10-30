# Generated by Django 4.0.6 on 2022-10-19 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0027_alter_localcomercial_privatekeymercadopago_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localcomercial',
            name='privateKeyMercadopago',
        ),
        migrations.AddField(
            model_name='localcomercial',
            name='accessTokenMercadopago',
            field=models.CharField(default='--', max_length=60),
        ),
        migrations.AlterField(
            model_name='localcomercial',
            name='publicKeyMercadopago',
            field=models.CharField(max_length=60),
        ),
    ]
