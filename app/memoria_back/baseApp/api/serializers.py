from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from baseApp.models import LocalComercial
from baseApp.models import Venta
from baseApp.models import ProductoVenta

from baseApp.models import Categoria
from baseApp.models import ProductoCategoria

from baseApp.models import Orden
from baseApp.models import ProductoOrden

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
    imagen = Base64ImageField()
    class Meta:
        model = Categoria
        fields= '__all__'

class CategoriaSerializer_put(ModelSerializer):
    imagen = Base64ImageField(required=False)
    class Meta:
        model = Categoria
        fields= ['nombre','descripcion','esVisible','esNuevo','imagen']
    
class CategoriaSerializer_get(ModelSerializer):
    class Meta:
        model = Categoria
        fields= '__all__'

class ProductoCategoriaSerializer_post(ModelSerializer):
    imagen = Base64ImageField(required=False)
    class Meta:
        model = ProductoCategoria
        fields= ['nombre','descripcion','esVisible','esNuevo','isBestProduct','imagen']
class ProductoCategoriaSerializer_get(ModelSerializer):
    class Meta:
        model = ProductoCategoria
        fields= '__all__'

class OrdenSerializer_get(ModelSerializer):
    class Meta:
        model = Orden
        fields= '__all__'
class OrdenSerializer_post(ModelSerializer):
    class Meta:
        model = Orden
        fields= '__all__'
class ProductoOrdenSerializer_get(ModelSerializer):
    class Meta:
        model = ProductoOrden
        fields= '__all__'
class ProductoOrdenSerializer_post(ModelSerializer):
    class Meta:
        model = ProductoOrden
        fields= '__all__'


