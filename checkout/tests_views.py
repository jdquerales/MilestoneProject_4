from django.test import TestCase
from products.models import Product
from .forms import OrderForm


class TestViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Product.objects.create(description='first product',
                               friendly_name='product', 
                               price=100, brand='some')

    def test_get_checkout_page(self):
        # This is the top level URL define in project admin
        response = self.client.get('/checkout/')
        self.assertRedirects(response, '/products/')

    def test_get_checkout_page_redirect_response(self):
        # This is the top level URL define in project admin
        response = self.client.get('/checkout/')
        self.assertEquals(response.status_code, 302)