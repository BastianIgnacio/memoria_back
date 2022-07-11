from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from baseApp.models import LocalComercial
from baseApp.models import Venta
from baseApp.models import ProductoVenta

from baseApp.models import Categoria
from baseApp.models import ProductoCategoria

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

class CategoriaSerializer_post(ModelSerializer):
    class Meta:
        model = Categoria
        fields= '__all__'
class CategoriaSerializer_get(ModelSerializer):
    class Meta:
        model = Categoria
        fields= '__all__'

class ProductoCategoriaSerializer_post(ModelSerializer):
    class Meta:
        model = ProductoCategoria
        fields= '__all__'
class ProductoCategoriaSerializer_get(ModelSerializer):
    class Meta:
        model = ProductoCategoria
        fields= '__all__'


