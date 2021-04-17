from django.test import TestCase
from .models import Product


class TestViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Product.objects.create(description='My product', friendly_name='product', price=100, brand='some')
    
    def test_get_products_page(self):
        response = self.client.get('/products/') # This is the top level URL define in project admin
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_product_detail_page(self):
        product = Product.objects.get(pk=1)
        response = self.client.get(f'/products/{product.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
