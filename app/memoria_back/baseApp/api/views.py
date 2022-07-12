from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from baseApp.models import LocalComercial
from baseApp.models import Venta
from baseApp.models import ProductoVenta
from baseApp.models import Categoria
from baseApp.models import ProductoCategoria
from baseApp.models import Orden
from baseApp.models import ProductoOrden

from baseApp.api.serializers import LocalComercialSerializer_get, LocalComercialSerializer_post
from baseApp.api.serializers import VentaSerializer_get, VentaSerializer_post
from baseApp.api.serializers import ProductoVentaSerializer_get, ProductoVentaSerializer_post
from baseApp.api.serializers import CategoriaSerializer_get, CategoriaSerializer_post
from baseApp.api.serializers import ProductoCategoriaSerializer_get, ProductoCategoriaSerializer_post
from baseApp.api.serializers import OrdenSerializer_get,OrdenSerializer_post
from baseApp.api.serializers import ProductoOrdenSerializer_get, ProductoOrdenSerializer_post

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
        serializer = VentaSerializer_get(Venta.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self, request):
        serializer = VentaSerializer_post(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED,data=serializer.data)

class VentaApiView_Detail(APIView):
    """
    Retrieve, update or delete a Venta instance.
    """
    def get(self, request, pk, format=None):
        try:
            venta = Venta.objects.get(id=pk)
        except Venta.DoesNotExist:
            raise Http404
        serializer = VentaSerializer_get(venta, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            put = Venta.objects.get(id=pk)
        except Venta.DoesNotExist:
            raise Http404
        serializer = VentaSerializer_post(put, data=request.data)
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

class ProductoVentaApiView(APIView):
    """
    List all ProductoVenta, or create a new ProductoVenta.
    """
    def get(self, request):
        serializer = ProductoVentaSerializer_get(ProductoVenta.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self, request):
        serializer = ProductoVentaSerializer_post(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED,data=serializer.data)

class ProductoVentaApiView_Detail(APIView):
    """
    Retrieve, update or delete a ProductoVenta instance.
    """
    def get(self, request, pk, format=None):
        try:
            pv = ProductoVenta.objects.get(id=pk)
        except ProductoVenta.DoesNotExist:
            raise Http404
        serializer = ProductoVentaSerializer_get(pv, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            put = ProductoVenta.objects.get(id=pk)
        except ProductoVenta.DoesNotExist:
            raise Http404
        serializer = ProductoVentaSerializer_post(put, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            pv = ProductoVenta.objects.get(id=pk)
        except ProductoVenta.DoesNotExist:
            raise Http404
        pv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoriaApiView(APIView):
    """
    List all Categoria, or create a new Categoria.
    """
    def get(self, request):
        serializer = CategoriaSerializer_get(Categoria.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self, request):
        serializer = CategoriaSerializer_post(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED,data=serializer.data)

class CategoriaApiView_Detail(APIView):
    """
    Retrieve, update or delete a Categoria instance.
    """
    def get(self, request, pk, format=None):
        try:
            cat = Categoria.objects.get(id=pk)
        except Categoria.DoesNotExist:
            raise Http404
        serializer = CategoriaSerializer_get(cat, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            put = Categoria.objects.get(id=pk)
        except Categoria.DoesNotExist:
            raise Http404
        serializer = CategoriaSerializer_post(put, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            cat = Categoria.objects.get(id=pk)
        except Categoria.DoesNotExist:
            raise Http404
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductoCategoriaApiView(APIView):
    """
    List all ProductoCategoria, or create a new ProductoCategoria.
    """
    def get(self, request):
        serializer = ProductoCategoriaSerializer_get(ProductoCategoria.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self, request):
        serializer = ProductoCategoriaSerializer_post(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED,data=serializer.data)

class ProductoCategoriaApiView_Detail(APIView):
    """
    Retrieve, update or delete a ProductoCategoria instance.
    """
    def get(self, request, pk, format=None):
        try:
            prod = ProductoCategoria.objects.get(id=pk)
        except ProductoCategoria.DoesNotExist:
            raise Http404
        serializer = ProductoCategoriaSerializer_get(prod, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            put = ProductoCategoria.objects.get(id=pk)
        except ProductoCategoria.DoesNotExist:
            raise Http404
        serializer = ProductoCategoriaSerializer_post(put, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            prod = ProductoCategoria.objects.get(id=pk)
        except ProductoCategoria.DoesNotExist:
            raise Http404
        prod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrdenApiView(APIView):
    """
    List all Orden, or create a new Orden.
    """
    def get(self, request):
        serializer = OrdenSerializer_get(Orden.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self, request):
        serializer = OrdenSerializer_post(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED,data=serializer.data)

class OrdenApiView_Detail(APIView):
    """
    Retrieve, update or delete a Orden instance.
    """
    def get(self, request, pk, format=None):
        try:
            orden = Orden.objects.get(id=pk)
        except Orden.DoesNotExist:
            raise Http404
        serializer = OrdenSerializer_get(orden, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            put = Orden.objects.get(id=pk)
        except Orden.DoesNotExist:
            raise Http404
        serializer = OrdenSerializer_post(put, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            orden = Orden.objects.get(id=pk)
        except Orden.DoesNotExist:
            raise Http404
        orden.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductoOrdenApiView(APIView):
    """
    List all ProductoOrden, or create a new ProductoOrden.
    """
    def get(self, request):
        serializer = ProductoOrdenSerializer_get(ProductoOrden.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self, request):
        serializer = ProductoOrdenSerializer_post(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED,data=serializer.data)

class ProductoOrdenApiView_Detail(APIView):
    """
    Retrieve, update or delete a ProductoOrden instance.
    """
    def get(self, request, pk, format=None):
        try:
            productoOrden = ProductoOrden.objects.get(id=pk)
        except ProductoOrden.DoesNotExist:
            raise Http404
        serializer = ProductoOrdenSerializer_get(productoOrden, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            put = ProductoOrden.objects.get(id=pk)
        except ProductoOrden.DoesNotExist:
            raise Http404
        serializer = ProductoOrdenSerializer_post(put, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            productoOrden = ProductoOrden.objects.get(id=pk)
        except ProductoOrden.DoesNotExist:
            raise Http404
        productoOrden.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)