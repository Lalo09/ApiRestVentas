from rest_framework import serializers
from .models import Sale, SaleDetail

class VentaReporteSerializer(serializers.ModelSerializer):
    """Serializador para ver las ventas en detalle"""

    productos = serializers.SerializerMethodField() #Crear nuevo campo

    class Meta:
        model = Sale
        fields = (
            'id',
            'date_sale',
            'amount',
            'count',
            'type_invoce',
            'cancelado',
            'type_payment',
            'state',
            'adreese_send',
            'user',
            'productos' #llamar ese nuevo campo
        )

    def get_productos(self,obj): #Obj representa cada uno de los objetos
        """Funcion para traer todos los productos de esa venta"""
        """Esta funcion se manda a llamar desde arriba con el SerializerMethodField"""
        query = SaleDetail.objects.productos_por_venta(obj.id) #Mandar a llamar manager'{}
        prudctos_serializados = DetalleVentaProductoSerializer(query,many=True).data #Mandar a llamar serializador de detalle de producto
        return prudctos_serializados

class DetalleVentaProductoSerializer(serializers.ModelSerializer):
    """Serializador de detalle de venta"""
    
    class Meta:
        model = SaleDetail
        fields = (
            'id',
            'sale',
            'product',
            'count',
            'price_purchase',
            'price_sale'
        )

class ProductoDetailSerializer(serializers.Serializer):
    """Serializador para producto y ponerlo en el proceso"""

    pk = serializers.IntegerField()
    count = serializers.IntegerField()

class ProcesoVentaSerializer(serializers.Serializer):
    """Serializador manual(No depende de un modelo)"""

    #Estructurar como quiero que el front end me envie una venta
    type_invoce = serializers.CharField()
    type_payment = serializers.CharField()
    adreese_send = serializers.CharField()
    productos = ProductoDetailSerializer(many=True) #Asignar serializer