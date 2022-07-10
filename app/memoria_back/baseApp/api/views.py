from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from baseApp.models import LocalComercial
from baseApp.api.serializers import LocalComercialSerializer_get, LocalComercialSerializer_post


class LocalComercialApiView(APIView):
    def get(self, request):
        serializer = LocalComercialSerializer_get(LocalComercial.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self, request):
        serializer = LocalComercialSerializer_post(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED,data=serializer.data)