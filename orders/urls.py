from django.urls import path
from . import views

urlpatterns = [
    path(
        'orders/',
        views.OrdenListCreateView.as_view(),
        name='orders-list'
    ),

    path(
        'order/<int:id>/',
        views.OrderDetailView.as_view(),
        name='order-detail'
    )
]
