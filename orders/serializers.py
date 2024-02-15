from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductSerializer
from supermarkets.serializers import SupermarketSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    class Meta:
        model = OrderItem
        fields = '__all__'

    def get_product(self, obj):
        product_data = {
            'id': obj.product.id,
            'name': obj.product.name,
            'value': obj.product.value
        }

        return product_data


class OrderSerializer(serializers.ModelSerializer):
    supermarket = SupermarketSerializer()
    order_items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = '__all__'
