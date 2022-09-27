from distutils.command.upload import upload
from tkinter import CASCADE
from unittest.mock import DEFAULT
from django.db import models
from user.models import User
import datetime
from PIL import Image

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
    privateKeyMercadopago = models.CharField(max_length=50)
    publicKeyMercadopago = models.CharField(max_length=50)
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
    fecha = models.DateTimeField(auto_now_add=True)
    refLocalComercial = models.ForeignKey(LocalComercial,on_delete=models.CASCADE,default=1)

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

        if img.height > 400 or img.width > 400:
            output_size = (400,400)
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

        if img.height > 400 or img.width > 400:
            output_size = (400,400)
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