from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from baseApp.models import LocalComercial
from baseApp.models import Venta

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

class VentaSelializer_get(ModelSerializer):
    class Meta:
        model = Venta
        fields= '__all__'

class VentaSelializer_post(ModelSerializer):
    class Meta:
        model = Venta
        fields= '__all__'
        