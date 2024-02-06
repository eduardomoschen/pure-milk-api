from django.urls import path
from . import views

urlpatterns = [
    path(
        'sellers/',
        views.SellerListCreateView.as_view(),
        name='sellers-list'
    ),
    path(
        'seller/<str:username>',
        views.SellerDetailView.as_view(),
        name='seller-detail'
    )
]
