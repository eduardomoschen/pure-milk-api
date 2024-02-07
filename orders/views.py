from rest_framework import generics
from django.db.models import Q
from .serializers import OrderSerializer
from .models import Order


class OrdenListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', None)

        if query:
            queryset = Order.objects.filter(Q(name__icontains=query))
        else:
            queryset = Order.objects.all()

        return queryset


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'
