from httplib2 import Response
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Colors, Product

from .serializers import ColorSerializer, ProductSerializer, PaginationSerializer,ProductSerializerViewSet

#Viewset de colors, crud completo
class ColorViewSet(viewsets.ModelViewSet):

    serializer_class = ColorSerializer #Se indica el serializer
    queryset = Colors.objects.all() #Consulta modelo

class ProductViewSet(viewsets.ModelViewSet):
    
    serializer_class = ProductSerializerViewSet
    queryset = Product.objects.all()
    pagination_class = PaginationSerializer #Asignar paginacion serializer

    #Sobreescribir metodo para agregar/quitar funcionalidades
    #def create(self,request):
     #   print(request.data) #Recuperar objeto que se envia
      #  return Response({'code':'200 Exito'})

    def perform_create(self,serializer):#Hacer cambios
        serializer.save(
            video = "https://www.youtube.com/watch?v=rfBlRXfnUFM"
        )