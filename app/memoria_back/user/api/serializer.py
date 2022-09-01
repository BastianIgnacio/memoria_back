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

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apellido = validated_data.get('apellido', instance.apellido)
        instance.rol = validated_data.get('rol', instance.rol)
        instance.telefono = validated_data.get('telefono', instance.telefono)
        instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance
        
class UserSerializer_put(ModelSerializer):
    nombre = serializers.CharField(required = True)
    apellido = serializers.CharField(required = True)
    rol = serializers.CharField(required = True)
    telefono = serializers.CharField(required = True)
    password =  serializers.CharField(required = False)
    class Meta:
        model = User
        fields = ['username', 'email',
                  'nombre', 'apellido', 'rol', 'telefono','password']

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apellido = validated_data.get('apellido', instance.apellido)
        instance.rol = validated_data.get('rol', instance.rol)
        instance.telefono = validated_data.get('telefono', instance.telefono)

        password = validated_data.get('password')
        if password is not None:
            instance.set_password(validated_data.get('password', instance.password))
            instance.save()
            return instance
        else:
            instance.save()
            return instance




class UserSerializer_get(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email', 'password',
                  'nombre', 'apellido', 'rol', 'telefono', 'refTienda']

