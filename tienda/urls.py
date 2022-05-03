from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('',include('applications.users.urls')),
    re_path('',include('applications.producto.urls')),
    re_path('',include('applications.venta.urls')),
    re_path('',include('applications.producto.routers')),
]
