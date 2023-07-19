from django.urls import path
from .views import CatShopList, CatShopDetail

urlpatterns = [
    path('cats/', CatShopList.as_view(), name='cat-list'),
    path('cats/<int:pk>/', CatShopDetail.as_view(), name='cat-detail'),
]
