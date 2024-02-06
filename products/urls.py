from django.urls import path
from . import views

urlpatterns = [
    path(
        'products/',
        views.ProductListCreateView.as_view(),
        name='products-list'
    ),
    path(
        'product/<str:name>',
        views.ProductDetailView.as_view(),
        name='product-detail'
    ),
]
