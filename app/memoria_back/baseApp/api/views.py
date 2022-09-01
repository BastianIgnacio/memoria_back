from msilib.schema import Feature
from coreapi import Link
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date, datetime
from django.http import Http404

from baseApp.models import LocalComercial
from baseApp.models import Venta
from baseApp.models import ProductoVenta
from baseApp.models import Categoria
from baseApp.models import ProductoCategoria
from baseApp.models import Orden
from baseApp.models import ProductoOrden

from baseApp.api.serializers import LocalComercialSerializer_get, LocalComercialSerializer_post, LocalComercialSerializer_put
from baseApp.api.serializers import VentaSerializer_get, VentaSerializer_post
from baseApp.api.serializers import ProductoVentaSerializer_get, ProductoVentaSerializer_post
from baseApp.api.serializers import CategoriaSerializer_get, CategoriaSerializer_post, CategoriaSerializer_put
from baseApp.api.serializers import ProductoCategoriaSerializer_get, ProductoCategoriaSerializer_post
from baseApp.api.serializers import OrdenSerializer_get, OrdenSerializer_post
from baseApp.api.serializers import ProductoOrdenSerializer_get, ProductoOrdenSerializer_post

from rest_framework.pagination import LimitOffsetPagination

class LocalComercialApiView(APIView, LimitOffsetPagination):
    """
    List all LocalComercial, or create a new LocalComercial.
    """

    def get(self, request):
        queryset = LocalComercial.objects.all()
        link = request.query_params.get('link')

        if link is not None:
           queryset = queryset.filter(link=link)
        
        results = self.paginate_queryset(queryset,request)
        serializer = LocalComercialSerializer_get(results, many=True)
        return self.get_paginated_response(serializer.data)
    
    def post(self, request):
        serializer = LocalComercialSerializer_post(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)


class LocalComercialApiView_Detail(APIView):
    """
    Retrieve, update or delete a LocalComercial instance.
    """

    def get(self, request, pk, format=None):
        try:
            locales = LocalComercial.objects.get(id=pk)
        except LocalComercial.DoesNotExist:
            raise Http404
        serializer = LocalComercialSerializer_get(locales)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            put = LocalComercial.objects.get(id=pk)
        except LocalComercial.DoesNotExist:
            raise Http404
        serializer = LocalComercialSerializer_put(put, data=request.data)
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


class VentaApiView(APIView, LimitOffsetPagination):
    """
    List all Venta, or create a new Venta.
    """

    def get(self, request):
        queryset = Venta.objects.all()
        refLocalComercial = request.query_params.get('refLocalComercial')
        fecha = request.query_params.get('fecha')

        if refLocalComercial is not None:
            queryset = queryset.filter(refLocalComercial=refLocalComercial)
        
        if fecha is not None:
            fecha_dateTime = datetime.strptime(fecha,'%Y-%m-%d')
            year = fecha_dateTime.year
            month = fecha_dateTime.month
            day = fecha_dateTime.day
            queryset = queryset.filter(fecha__year=year, fecha__month= month, fecha__day=day)
        
        results = self.paginate_queryset(queryset,request)
        serializer = VentaSerializer_get(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = VentaSerializer_post(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)


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


class ProductoVentaApiView(APIView, LimitOffsetPagination):
    """
    List all ProductoVenta, or create a new ProductoVenta.
    """

    def get(self, request):
        queryset = ProductoVenta.objects.all()
        refVenta = request.query_params.get('refVenta')

        if refVenta is not None:
            queryset = queryset.filter(refVenta=refVenta)
        
        results = self.paginate_queryset(queryset,request)
        serializer = ProductoVentaSerializer_get(results, many=True)
        return self.get_paginated_response(serializer.data)
    def post(self, request):
        serializer = ProductoVentaSerializer_post(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)


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


class CategoriaApiView(APIView, LimitOffsetPagination):
    """
    List all Categoria, or create a new Categoria.
    """
    def get(self, request):
        queryset = Categoria.objects.all()
        refLocalComercial = request.query_params.get('refLocalComercial')
        esNuevo = request.query_params.get('esNuevo')

        if refLocalComercial is not None:
            queryset = queryset.filter(refLocalComercial=refLocalComercial)
        
        if esNuevo is not None:
            queryset = queryset.filter(esNuevo=esNuevo)
        
        results = self.paginate_queryset(queryset,request)
        serializer = CategoriaSerializer_get(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = CategoriaSerializer_post(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)


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
        serializer = CategoriaSerializer_put(put, data=request.data)
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


class ProductoCategoriaApiView(APIView, LimitOffsetPagination):
    """
    List all ProductoCategoria, or create a new ProductoCategoria.
    """

    def get(self, request):
        queryset = ProductoCategoria.objects.all()
        refCategoria = request.query_params.get('refCategoria')

        if refCategoria is not None:
            queryset = queryset.filter(refCategoria=refCategoria)
        
        results = self.paginate_queryset(queryset,request)
        serializer = ProductoCategoriaSerializer_get(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = ProductoCategoriaSerializer_post(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)


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


class OrdenApiView(APIView, LimitOffsetPagination):
    """
    List all Orden, or create a new Orden.
    """

    def get(self, request):
        queryset = Orden.objects.all()
        refVenta = request.query_params.get('refVenta')
        refLocalComercial = request.query_params.get('refLocalComercial')
        estado = request.query_params.get('estado')

        if refVenta is not None:
            queryset = queryset.filter(refVenta=refVenta)
        
        if refLocalComercial is not None:
            queryset = queryset.filter(refLocalComercial=refLocalComercial)
        
        if estado is not None:
            queryset = queryset.filter(estado=estado)
        
        results = self.paginate_queryset(queryset,request)
        serializer = OrdenSerializer_get(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = OrdenSerializer_post(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)


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


class ProductoOrdenApiView(APIView, LimitOffsetPagination):
    """
    List all ProductoOrden, or create a new ProductoOrden.
    """

    def get(self, request):
        queryset = ProductoOrden.objects.all()
        refOrden = request.query_params.get('refOrden')

        if refOrden is not None:
            queryset = queryset.filter(refOrden=refOrden)
        
        results = self.paginate_queryset(queryset,request)
        serializer = ProductoOrdenSerializer_get(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = ProductoOrdenSerializer_post(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)


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
