from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from baseApp.models import LocalComercial
from baseApp.models import Venta
from baseApp.models import ProductoVenta

class LocalComercialSerializer_get(ModelSerializer):
    class Meta:
        model = LocalComercial
        fields = ['id','nombre','direccion','link','horarioAtencion','tieneDelivery','estado',
        'tieneMercadopago']  
class LocalComercialSerializer_post(ModelSerializer):
    class Meta:
        model = LocalComercial
        fields = ['id','nombre','direccion','link','horarioAtencion','tieneDelivery','estado','publicKeyMercadopago',
        'privateKeyMercadopago','tieneMercadopago']

class VentaSerializer_get(ModelSerializer):
    class Meta:
        model = Venta
        fields= '__all__'
class VentaSerializer_post(ModelSerializer):
    class Meta:
        model = Venta
        fields= '__all__'

class ProductoVentaSerializer_get(ModelSerializer):
    class Meta:
        model = ProductoVenta
        fields = ['id','refVenta','total','cantidad','precioUnitario','nombreProducto','descripcionProducto','notaEspecial']
class ProductoVentaSerializer_post(ModelSerializer):
    class Meta:
        model = ProductoVenta
        fields = ['id','total','cantidad','precioUnitario','nombreProducto','descripcionProducto','notaEspecial']
