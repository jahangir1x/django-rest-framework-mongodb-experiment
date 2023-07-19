from rest_framework import generics
from .models import CatShop
from .serializers import CatShopSerializer


class CatShopList(generics.ListCreateAPIView):
    queryset = CatShop.objects.all()
    serializer_class = CatShopSerializer


class CatShopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CatShop.objects.all()
    serializer_class = CatShopSerializer
