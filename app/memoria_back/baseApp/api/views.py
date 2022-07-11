from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from baseApp.models import LocalComercial
from baseApp.models import Venta
from baseApp.api.serializers import LocalComercialSerializer_get, LocalComercialSerializer_post, VentaSelializer_get, VentaSelializer_post


class LocalComercialApiView(APIView):
    """
    List all LocalComercial, or create a new LocalComercial.
    """
    def get(self, request):
        serializer = LocalComercialSerializer_get(LocalComercial.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self, request):
        serializer = LocalComercialSerializer_post(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED,data=serializer.data)

class LocalComercialApiView_Detail(APIView):
    """
    Retrieve, update or delete a LocalComercial instance.
    """
    def get(self, request, pk, format=None):
        try:
            locales = LocalComercial.objects.get(id=pk)
        except LocalComercial.DoesNotExist:
            raise Http404
        serializer = LocalComercialSerializer_get(locales, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            put = LocalComercial.objects.get(id=pk)
        except LocalComercial.DoesNotExist:
            raise Http404
        serializer = LocalComercialSerializer_post(put, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            local = LocalComercial.objects.get(id=pk)
        except LocalComercial.DoesNotExist:
            raise Http404
        local.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class VentaApiView(APIView):
    """
    List all Venta, or create a new Venta.
    """
    def get(self, request):
        serializer = VentaSelializer_get(Venta.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self, request):
        serializer = VentaSelializer_post(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED,data=serializer.data)

class VentaApiView_Detail(APIView):
    """
    Retrieve, update or delete a LocalComercial instance.
    """
    def get(self, request, pk, format=None):
        try:
            venta = Venta.objects.get(id=pk)
        except Venta.DoesNotExist:
            raise Http404
        serializer = VentaSelializer_get(venta, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            put = Venta.objects.get(id=pk)
        except Venta.DoesNotExist:
            raise Http404
        serializer = VentaSelializer_post(put, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            local = Venta.objects.get(id=pk)
        except Venta.DoesNotExist:
            raise Http404
        local.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)