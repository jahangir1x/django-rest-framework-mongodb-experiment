from rest_framework.test import APITestCase
from django.urls import reverse
from .models import CatShop


# create new cat
class CatCreateTest(APITestCase):
    def setUp(self):
        self.url = reverse('cat-list')

    def test_create_product(self):
        data = {
            "name": "Fluffy",
            "price": 1234.99,
            "breed": "Persian",
            "description": "A cute and fluffy Persian cat."
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(CatShop.objects.count(), 1)
        self.assertEqual(CatShop.objects.get().name, 'Fluffy')

# get all cats

# get a cat

# modify a cat

# delete a cat