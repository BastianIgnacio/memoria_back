from tkinter import CASCADE
from django.db import models
import datetime

# Create your models here.
""" Clase LocalComercial representa una tienda virtual"""
class LocalComercial(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField()
    link = models.CharField(max_length=255)
    horarioAtencion = models.TextField()
    tieneDelivery = models.BooleanField(default=False)
    estado = models.CharField(max_length=20)
    privateKeyMercadopago = models.CharField(max_length=25)
    publicKeyMercadopago = models.CharField(max_length=25)
    tieneMercadopago = models.BooleanField(default=False)

""" Clase Venta representa una venta de una tienda virtual """
class Venta(models.Model):
    total = models.IntegerField()
    tipoPago = models.CharField(max_length=50)
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
    notaEspecial = models.TextField()
    refVenta = models.ForeignKey(Venta,on_delete=models.CASCADE,default=1)

""" Clase Categoria representa una CATEGORIA de una tienda virtual """
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    esVisible = models.BooleanField(default=False)
    esNuevo = models.BooleanField(default=True)
    refLocalComercial = models.ForeignKey(LocalComercial,on_delete=models.CASCADE,default=1)

""" Clase ProductoCategoria representa un PRODUCTO de una CATEGORIA de una tienda virtual """
class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    esVisible = models.BooleanField(default=False)
    esNuevo = models.BooleanField(default=True)
    isBestProduct = models.BooleanField(default=False)
    refCategoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,default=1)


"""Clase Orden representa una ORDEN que se le ha realizado a una tienda virtual"""
class Orden(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    tipoEntrega = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    direccionEntrega = models.TextField()
    telefonoEntrega = models.CharField(max_length=50)
    nombrePedido = models.CharField(max_length=50)
    precioEnvio = models.IntegerField()
    total = models.IntegerField()
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