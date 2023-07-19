from rest_framework import serializers
from .models import CatShop


# CatShop model serializer
class CatShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatShop
        fields = [
            'id',
            'name',
            'price',
            'breed',
            'description',
        ]
