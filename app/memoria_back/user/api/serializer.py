from rest_framework.serializers import ModelSerializer
from user.models import User


class UserSerializer_post(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'nombre', 'apellido', 'rol', 'telefono']


class UserSerializer_get(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
