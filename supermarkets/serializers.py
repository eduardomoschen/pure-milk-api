from rest_framework import serializers
from .models import Supermarket


class SupermarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supermarket
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['cnpj'] = instance.formatted_cnpj()
        representation['phone_number'] = instance.formatted_phone_number()

        return representation
