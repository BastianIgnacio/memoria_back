from rest_framework.serializers import ModelSerializer
from baseApp.models import LocalComercial

class LocalComercialSerializer_get(ModelSerializer):
    class Meta:
        model = LocalComercial
        fields = ['nombre','direccion','link','horarioAtencion','tieneDelivery','estado',
        'tieneMercadopago']
    
class LocalComercialSerializer_post(ModelSerializer):
    class Meta:
        model = LocalComercial
        fields = ['nombre','direccion','link','horarioAtencion','tieneDelivery','estado','publicKeyMercadopago',
        'privateKeyMercadopago','tieneMercadopago']