from rest_framework import generics
from django.db.models import Q
from .models import Supermarket
from .serializers import SupermarketSerializer


class SupermarketListCreateView(generics.ListCreateAPIView):
    serializer_class = SupermarketSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', None)

        if query:
            queryset = Supermarket.objects.filter(Q(name__icontains=query))
        else:
            queryset = Supermarket.objects.all()

        return queryset


class SupermarketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supermarket.objects.all()
    serializer_class = SupermarketSerializer
    lookup_field = 'name'
