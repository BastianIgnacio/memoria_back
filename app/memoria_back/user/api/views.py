from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.http import Http404

from django.contrib.auth import authenticate

from user.models import User
from user.api.serializer import UserSerializer_post, UserSerializer_get

from rest_framework_simplejwt.views import TokenObtainPairView 
from rest_framework_simplejwt.tokens import RefreshToken

from user.api.serializer import CustomTokenObtairPairSerializer

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtairPairSerializer

    def post(self, request, *arg, **kwargs):
        email = request.data.get('email', '')
        password = request.data.get('password', '')
        user = authenticate(
            email=email,
            password=password
        )
        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = UserSerializer_get(user)
                return Response({
                    'token' : login_serializer.validated_data.get('access'),
                    'refresh' : login_serializer.validated_data.get('refresh'),
                    'user' : user_serializer.data,
                    'message' : 'Inicio de sesion exitoso'
                }, status=status.HTTP_200_OK)
        return Response({'error':'Contraseña o nombre de usuario incorrecto'}, status=status.HTTP_400_BAD_REQUEST)

class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user', ''))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Sesion cerrada correctamente.'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe este usuario.'}, status=status.HTTP_400_BAD_REQUEST)




class UserApiView(APIView):
    """
    List all LocalComercial, or create a new LocalComercial.
    """

    def get(self, request):
        serializer = UserSerializer_get(User.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request):
        serializer = UserSerializer_post(data=request.POST,required=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)


class UserApiView_Detail(APIView):
    """
    Retrieve, update or delete a LocalComercial instance.
    """

    def get(self, request, pk, format=None):
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404
        serializer = UserSerializer_get(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            put = User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404
        serializer = UserSerializer_post(put, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
