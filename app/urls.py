from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('products.urls')),
    path('api/v1/', include('sellers.urls')),
    path('api/v1/', include('supermarkets.urls')),
    path('api/v1/', include('orders.urls')),
]
