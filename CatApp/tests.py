from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import CatShop


# create new cat
class CatCreateTest(APITestCase):
    def setUp(self):
        self.url = reverse('cat-list')

    def test_create_cat(self):
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


class CatGetAllTest(APITestCase):
    def setUp(self):
        self.cat1 = CatShop.objects.create(
            name='Fluffy', price=1234.99, breed="Persian", description='A cute and fluffy Persian cat.')
        self.cat2 = CatShop.objects.create(
            name='Whiskers', price=9343.99, breed="Siamese", description='An elegant Siamese cat with beautiful blue eyes.')
        self.url = reverse('cat-list')

    def test_get_cats(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 2)

# get a cat


class CatGetTest(APITestCase):
    def setUp(self):
        self.cat = CatShop.objects.create(
            name='Fluffy', price=1234.99, breed="Persian", description='A cute and fluffy Persian cat.')
        self.url = reverse('cat-detail', args=[self.cat.pk])

    def test_get_cat(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 5)

# modify a cat


class CatModifyTest(APITestCase):
    def setUp(self):
        self.cat = CatShop.objects.create(
            name='Fluffy', price=1234.99, breed="Persian", description='A cute and fluffy Persian cat.')
        self.url = reverse('cat-detail', args=[self.cat.pk])

    def test_modify_cat(self):
        data = {
            "name": "Whiskers",
            "price": 1234.99,
            "breed": "Persian",
            "description": "A cute and fluffy Persian cat."
        }

        response = self.client.put(self.url, data, format='json')
        self.assertEqual(CatShop.objects.get().name, 'Whiskers')

# delete a cat


class CatDeleteTest(APITestCase):
    def setUp(self):
        self.cat = CatShop.objects.create(
            name='Fluffy', price=1234.99, breed="Persian", description='A cute and fluffy Persian cat.')
        self.url = reverse('cat-detail', args=[self.cat.pk])

    def test_delete_cat(self):
        response = self.client.delete(self.url)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
