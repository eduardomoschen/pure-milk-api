from rest_framework import serializers
from .models import Seller


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['phone_number'] = instance.formatted_phone_number()
        representation['salary'] = instance.formatted_salary()

        return representation
