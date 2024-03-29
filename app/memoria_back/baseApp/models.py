from distutils.command.upload import upload
from tkinter import CASCADE
from unittest.mock import DEFAULT
from urllib import response
from django.db import models
from requests import request
from user.models import User
import datetime
import time
import threading
from PIL import Image
import requests


# Create your models here.
""" Clase LocalComercial representa una tienda virtual"""
class LocalComercial(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField()
    link = models.CharField(max_length=64, unique=True)
    horarioAtencion = models.TextField()
    tieneDelivery = models.BooleanField(default=False)
    tieneRetiroLocal = models.BooleanField(default=False)
    estado = models.CharField(max_length=20)
    abierto = models.BooleanField(default=False)
    accessTokenMercadopago = models.CharField(max_length=80,default='--')
    publicKeyMercadopago = models.CharField(max_length=80)
    tieneMercadopago = models.BooleanField(default=False)
    pagoRetiroLocalEfectivo = models.BooleanField(default=False);
    pagoRetiroLocalPos = models.BooleanField(default=False);
    pagoRetiroLocalMercadopago = models.BooleanField(default=False);
    pagoDeliveryEfectivo = models.BooleanField(default=False);
    pagoDeliveryPos = models.BooleanField(default=False);
    pagoDeliveryMercadopago = models.BooleanField(default=False);
    imagen = models.ImageField(blank='',default="",upload_to='fotos/localesComerciales')
    habilitado = models.BooleanField(default=False);
    region = models.CharField(max_length=50, default="SIN REGIÓN")
    comuna = models.CharField(max_length=50, default="SIN COMUNA")
    telefono = models.CharField(max_length=12, default="+569XXXXXXX")

""" Clase Venta representa una venta de una tienda virtual """
class Venta(models.Model):
    total = models.IntegerField()
    tipoPago = models.CharField(max_length=50)
    estadoPago = models.CharField(max_length=50, default='NO_PAGADO')
    estadoVenta = models.CharField(max_length=50, default='EN_PROCESO')
    pagadoViaMercadopago = models.BooleanField(default=False)
    mercadopago_external_reference = models.CharField(max_length=100, default='-')
    mercadopago_preference_id = models.CharField(max_length=100, default='-')
    mercadopago_status = models.CharField(max_length=100, default='-')
    mercadopago_payment_id = models.CharField(max_length=100, default='-')
    mercadopago_collection_id = models.CharField(max_length=100, default='-')
    mercadopago_collection_status = models.CharField(max_length=100, default='-')
    mercadopago_merchant_order_id = models.CharField(max_length=100, default='-')
    fecha = models.DateTimeField(auto_now_add=True)
    refLocalComercial = models.ForeignKey(LocalComercial,on_delete=models.CASCADE,default=1)

    def updateEstadoPreference(preferenceId):
        time.sleep(3)
        print("Primer llamado a la api usando hilos")
        print(preferenceId)
        time.sleep(3)
        print("Segundo llamado a la  api usando hilos")
        print(preferenceId)
        time.sleep(3)
        print("Tercer llamado a la api usando hilos")
        print(preferenceId)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        
        if self.pagadoViaMercadopago:
            def updateEstadoPreference(external_reference):
                # Ahora teniendo el external_reference
                # Debemos llamar a la api de mercadopago
                # Ver el estado del pago
                # results.length === 0 --> no se ha pagado
                # results-length === 1 --> El pago se ha generado

                headers = {"Authorization": "Bearer TEST-1903893011363375-092614-91c2a1fe64a3aa4c783266504a8d39cc-152372056"}
                url = "https://api.mercadopago.com/v1/payments/search?external_reference="+external_reference

                time.sleep(10)
                print("Primer llamado a la api usando hilos")
                response = requests.get(url, headers=headers)
                print(response)

                time.sleep(15)
                print("Segundo llamado a la  api usando hilos")
                response = requests.get(url, headers=headers)
                print(response)

                time.sleep(15)
                print("Tercer llamado a la api usando hilos")
                response = requests.get(url, headers=headers)
                print(response)

                time.sleep(15)
                print("Cuarto llamado a la api usando hilos")
                response = requests.get(url, headers=headers)
                print(response)
            x = threading.Thread(target=updateEstadoPreference, args=(self.mercadopago_external_reference,))
            x.start()
    

""" Clase ProductoVenta representa un producto que tiene una venta, con la finalidad de obtener 
todos los productos que posee una venta """
class ProductoVenta(models.Model):
    total = models.IntegerField()
    cantidad = models.IntegerField()
    precioUnitario = models.IntegerField()
    nombreProducto = models.CharField(max_length=255)
    descripcionProducto = models.TextField()
    refVenta = models.ForeignKey(Venta,on_delete=models.CASCADE,default=1)

""" Clase Categoria representa una CATEGORIA de una tienda virtual """
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    esVisible = models.BooleanField(default=False)
    esNuevo = models.BooleanField(default=True)
    imagen = models.ImageField(blank='',default="",upload_to='fotos/categorias')
    refLocalComercial = models.ForeignKey(LocalComercial,on_delete=models.CASCADE,default=1)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img = Image.open(self.imagen.path)

        if img.height > 600 or img.width > 600:
            output_size = (600,600)
            img.thumbnail(output_size)
            img.save(self.imagen.path)

""" Clase ProductoCategoria representa un PRODUCTO de una CATEGORIA de una tienda virtual """
class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    esVisible = models.BooleanField(default=False)
    esNuevo = models.BooleanField(default=True)
    isBestProduct = models.BooleanField(default=False)
    imagen = models.ImageField(blank='',default="",upload_to='fotos/productos')
    refCategoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,default=1)
    precio = models.IntegerField(default=0)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img = Image.open(self.imagen.path)

        if img.height > 600 or img.width > 600:
            output_size = (600,600)
            img.thumbnail(output_size)
            img.save(self.imagen.path)


"""Clase Orden representa una ORDEN que se le ha realizado a una tienda virtual"""
class Orden(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    tipoEntrega = models.CharField(max_length=50)
    entregaDelivery = models.BooleanField(default=False)
    estado = models.CharField(max_length=50)
    direccionEntrega = models.TextField()
    telefonoEntrega = models.CharField(max_length=50)
    emailEntrega = models.EmailField(default='default@default.com')
    nombrePedido = models.CharField(max_length=50)
    precioEnvio = models.IntegerField()
    total = models.IntegerField()
    tiempoEntrega = models.CharField(max_length=255, default='Lo antes posible')
    refLocalComercial = models.ForeignKey(LocalComercial,on_delete=models.CASCADE,default=1)
    refVenta = models.ForeignKey(Venta,on_delete=models.CASCADE,default=1)

""" Clase  ProductoOrden representa a un producto que pertenece a una orden """
class ProductoOrden(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    notaEspecial = models.TextField()
    precioTotal = models.IntegerField()
    precioUnitario = models.IntegerField()
    cantidad = models.IntegerField()
    refOrden = models.ForeignKey(Orden,on_delete=models.CASCADE,default=1)