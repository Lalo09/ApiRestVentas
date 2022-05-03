from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .models import Product
from .serializers import ProductSerializer

class ListProductUser(ListAPIView):
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,) #Asignar tipo de autenticacion
    permission_classes = [IsAuthenticated] #Permisos

    def get_queryset(self):
        #Recuperar usuario
        print("*****")
        usuario = self.request.user
        print(usuario)
        return Product.objects.productos_por_usuario(usuario)

class ListProductStockUser(ListAPIView):

    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,IsAdminUser]

    def get_queryset(self):
       return Product.objects.productos_con_stock()

class ListProductGenero(ListAPIView):
    
    serializer_class = ProductSerializer

    def get_queryset(self):
        genero = self.kwargs['gender'] #Recuperar parametro por url
        return Product.objects.productos_por_genero(genero)
    
class FiltrarProductos(ListAPIView):
    
    serializer_class = ProductSerializer

    def get_queryset(self):

        varon = self.request.query_params.get('man',None) #Recojer parametros por url en rest
        mujer = self.request.query_params.get('woman',None)
        nombre = self.request.query_params.get('name',None)

        #la url se debe definir: 
        #http://127.0.0.1:8000/api/product/filtrar/?man=False&woman=True&name=a

        return Product.objects.filtrar_produtos(
            man = varon,
            woman = mujer,
            name = nombre
        )