from django.contrib import admin
from baseApp.models import LocalComercial, ProductoVenta, Venta

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