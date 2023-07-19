from rest_framework import generics
from .models import CatShop
from .serializers import CatShopSerializer


# handle /api/cats/ logic
# get, post
class CatShopList(generics.ListCreateAPIView):
    queryset = CatShop.objects.all()
    serializer_class = CatShopSerializer


# handle /api/cats/<int:pk>/ logic
# get, put, delete
class CatShopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CatShop.objects.all()
    serializer_class = CatShopSerializer
