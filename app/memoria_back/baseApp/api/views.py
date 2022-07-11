from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from baseApp.models import LocalComercial
from baseApp.api.serializers import LocalComercialSerializer_get, LocalComercialSerializer_post


class LocalComercialApiView(APIView):
    def get_object(self, pk):
        try:
            return LocalComercial.objects.get(pk=pk)
        except LocalComercial.DoesNotExist:
            raise Http404
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
    """
    Retrieve, update or delete a LocalComercial instance.
    """
    def get(self, request, format=None):
        locales = LocalComercial.objects.all()
        serializer = LocalComercialSerializer_get(locales, many=True)
        return Response(serializer.data)


    