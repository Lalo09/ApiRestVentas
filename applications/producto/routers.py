from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()

router.register(r'colors',viewsets.ColorViewSet,basename="colors") #Ruta que ya viene con get, post, update, delete
router.register(r'productos',viewsets.ProductViewSet,basename="productos")

urlpatterns = router.urls