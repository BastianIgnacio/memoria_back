from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from user.models import User


class UserSerializer_post(ModelSerializer):
    nombre = serializers.CharField(required = True)
    apellido = serializers.CharField(required = True)
    rol = serializers.CharField(required = True)
    telefono = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password',
                  'nombre', 'apellido', 'rol', 'telefono']


class UserSerializer_get(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password',
                  'nombre', 'apellido', 'rol', 'telefono']

