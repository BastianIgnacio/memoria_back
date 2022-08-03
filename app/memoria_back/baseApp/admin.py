from django.contrib import admin
from baseApp.models import LocalComercial
from baseApp.models import ProductoVenta, Venta
from baseApp.models import Categoria, ProductoCategoria
from baseApp.models import Orden, ProductoOrden

# Register your models here.
@admin.register(LocalComercial)
class LocalComercialAdmin(admin.ModelAdmin):
    list_display = ['nombre','link']

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ['fecha','total']

@admin.register(ProductoVenta)
class ProductoVentaAdmin(admin.ModelAdmin):
    list_display = ['nombreProducto','total','cantidad','precioUnitario']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre','esVisible','esNuevo']

@admin.register(ProductoCategoria)
class ProductoCategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre','esVisible','esNuevo','refCategoria']

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ['fecha','estado','refLocalComercial']

@admin.register(ProductoOrden)
class ProductoOrdenAdmin(admin.ModelAdmin):
    list_display = ['nombre','precioUnitario','cantidad','precioTotal','refOrden']