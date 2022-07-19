import imp
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from user.models import User
from user.api.serializer import UserSerializer_post, UserSerializer_get


class UserApiView(APIView):
    """
    List all LocalComercial, or create a new LocalComercial.
    """

    def get(self, request):
        serializer = UserSerializer_get(User.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request):
        serializer = UserSerializer_post(data=request.POST)
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
