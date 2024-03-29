"""memoria_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from baseApp.api.views import LocalComercialApiView, LocalComercialApiView_Detail
from baseApp.api.views import VentaApiView, VentaApiView_Detail
from baseApp.api.views import ProductoVentaApiView, ProductoVentaApiView_Detail
from baseApp.api.views import CategoriaApiView, CategoriaApiView_Detail
from baseApp.api.views import ProductoCategoriaApiView, ProductoCategoriaApiView_Detail
from baseApp.api.views import OrdenApiView, OrdenApiView_Detail
from baseApp.api.views import ProductoOrdenApiView, ProductoOrdenApiView_Detail
from baseApp.api.views import mercadoPagoApiView

# Aca tenemos el endpoint para los Mejores Productos
from baseApp.api.views import ProductoCategoriaMejoresProductos

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="MYSYSTEM API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    #Rutas para JWT Auth 
    path('api/', include('user.api.router')),

    # Rutas para Local Comerical
    path('api/localComercials/',LocalComercialApiView.as_view()),
    path('api/localComercials/<int:pk>/',LocalComercialApiView_Detail.as_view()),

    # Rutas para Venta
    path('api/ventas/',VentaApiView.as_view()),
    path('api/ventas/<int:pk>/',VentaApiView_Detail.as_view()),

    # Rutas para ProductoVenta
    path('api/productoVentas/',ProductoVentaApiView.as_view()),
    path('api/productoVentas/<int:pk>/',ProductoVentaApiView_Detail.as_view()),

    #Rutas para Categoria
    path('api/categorias/',CategoriaApiView.as_view()),
    path('api/categorias/<int:pk>/',CategoriaApiView_Detail.as_view()),

    #Rutas para ProductoCategoria
    path('api/productoCategorias/',ProductoCategoriaApiView.as_view()),
    path('api/productoCategorias/<int:pk>/',ProductoCategoriaApiView_Detail.as_view()),

    #Ruta para MejoresProductos
    path('api/productoCategoriaMejoresProductos/',ProductoCategoriaMejoresProductos.as_view()),
    
    #Rutas para Orden
    path('api/ordens/',OrdenApiView.as_view()),
    path('api/ordens/<int:pk>/',OrdenApiView_Detail.as_view()),

    #Rutas para ProductoOrden
    path('api/productoOrdens/',ProductoOrdenApiView.as_view()),
    path('api/productoOrdens/<int:pk>/',ProductoOrdenApiView_Detail.as_view()),

    #Rutas para MERCADOPAGO
    path('api/mercadoPago/',mercadoPagoApiView.as_view()),



    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
