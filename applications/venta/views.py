from django.shortcuts import render
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView, CreateAPIView
)

from .models import Sale, SaleDetail

from applications.producto.models import Product

from .serializers import (
    VentaReporteSerializer,
    ProcesoVentaSerializer
)

class ReportVentasList(ListAPIView):

    serializer_class = VentaReporteSerializer #Definir el serializador

    def get_queryset(self):
        return Sale.objects.all()

class RegistrarVenta(CreateAPIView):
    authentication_classes = (TokenAuthentication,) #Definir que la autenticacion sea por token
    permission_classes = [IsAuthenticated] #Realizar accion solo si esta autenticado

    serializer_class = ProcesoVentaSerializer #Definir serializador

    #Reescribir funcion create de CreateAPIView
    def create(self,request,*args,**kwargs):

        #Deserializar json que hemos recibido
        serializer = ProcesoVentaSerializer(data=request.data) #Recibir data que hemos recibido

        #Indiciar si lo serializado es correcto
        serializer.is_valid(raise_exception = True)

        #Recuperar informacion del json
        #tipo_recibo=serializer.validated_data['type_invoce']
        #print('*******', tipo_recibo)

        #Guardar venta
        #Crear objeto de venta
        venta = Sale.objects.create(
            date_sale = timezone.now(),
            amount = 0,
            count =0,
            type_invoce = serializer.validated_data['type_invoce'],
            type_payment = serializer.validated_data['type_payment'],
            adreese_send = serializer.validated_data['adreese_send'],
            user = self.request.user,
        )

        #Variables para venta
        amount=0
        count=0

        #Recuperar los productos de la venta
        productos = serializer.validated_data['productos']
        #print(productos) #Ver como llegan los productos

        ventas_detalle = []

        for producto in productos:
            prod = Product.objects.get(id=producto['pk'])
            venta_detalle = SaleDetail(
                sale=venta,
                product = prod,
                count = producto['count'],
                price_purchase = prod.price_purchase,
                price_sale = prod.price_sale,
            )

            amount = amount + prod.price_sale*producto['count']
            count = count + producto['count']

            ventas_detalle.append(venta_detalle)

        #Actualizar venta con los nuevos valores
        venta.amount = amount
        venta.count = count
        venta.save()
       
        #Guardar producto (detalle de venta) en la venta ya realizada y actualizada
        SaleDetail.objects.bulk_create(ventas_detalle) #añadir todo un array al mismo tiempo

        return Response({'msj':"Venta exitosa"}) #Los create deben responder con un json, aqui se puede personalizar el mensaje y poner lo que sea