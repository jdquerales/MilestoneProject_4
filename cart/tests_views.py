from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product
import json


class TestViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Product.objects.create(description='first product',
                               friendly_name='product', price=100, brand='some')

    def test_get_shopping_cart_page(self):
        response = self.client.get('/cart/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')