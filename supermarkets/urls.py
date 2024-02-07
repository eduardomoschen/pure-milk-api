from django.urls import path
from . import views

urlpatterns = [
    path(
        'supermarkets/',
        views.SupermarketListCreateView.as_view(),
        name='supermarkets-list'
    ),

    path(
        'supermarket/<str:name>/',
        views.SupermarketDetailView.as_view(),
        name='supermarket-detail'
    )
]
