import email
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from user.models import User


class CustomTokenObtairPairSerializer(TokenObtainPairSerializer):
    pass

class UserSerializer_post(ModelSerializer):
    nombre = serializers.CharField(required = True)
    apellido = serializers.CharField(required = True)
    rol = serializers.CharField(required = True)
    telefono = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password',
                  'nombre', 'apellido', 'rol', 'telefono']

    def create(self, validated_data):
        user = User(
            username= validated_data['username'],
            email= validated_data['email'],
            nombre= validated_data['nombre'],
            apellido= validated_data['apellido'],
            rol= validated_data['rol'],
            telefono= validated_data['telefono']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer_get(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email', 'password',
                  'nombre', 'apellido', 'rol', 'telefono', 'refTienda']

