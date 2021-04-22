from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product
import json


class TestViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Product.objects.create(description='first product',
                               friendly_name='product', 
                               price=100, brand='some')

    def test_get_shopping_cart_page(self):
        response = self.client.get('/cart/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')

    def test_get_add_to_cart_page_302(self):
        product = Product.objects.get(pk=1)
        response = self.client.post(f'/cart/add/{product.id}/',
                                    {'quantity':'1', 
                                    'redirect_url':f'/products/{product.id}'})
        self.assertEquals(response.status_code, 302)

    def test_get_add_to_cart_page(self):
        product = Product.objects.get(pk=1)
        response = self.client.post(f'/cart/add/{product.id}/',
                                    {'quantity':'1', 
                                    'redirect_url':f'/products/{product.id}'})
        self.assertRedirects(response, f'/products/{product.id}')

