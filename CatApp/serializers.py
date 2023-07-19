from rest_framework import serializers
from .models import CatShop


class CatShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatShop
        fields = [
            'name',
            'price',
            'breed',
            'description',
        ]
