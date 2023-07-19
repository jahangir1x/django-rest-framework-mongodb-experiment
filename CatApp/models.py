from django.db import models


# CatShop model
class CatShop(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()
    breed = models.CharField(max_length=64)
    description = models.TextField()