from django.urls import include,re_path,path

from . import views

app_name = "producto_app"

urlpatterns = [
    path(
        'api/product/por-usuario',
        views.ListProductUser.as_view(),
        name = 'product-product_by_user'
    ),
    path(
        'api/product/con-stock',
        views.ListProductStockUser.as_view(),
        name = 'product-product_con_stock'
    ),
    path(
        'api/product/genero/<gender>/',
        views.ListProductGenero.as_view(),
        name = 'product-product_por_genero'
    ),
    path(
        'api/product/filtrar/',
        views.FiltrarProductos.as_view(),
        name = 'product-filtrar'
    ),
]
