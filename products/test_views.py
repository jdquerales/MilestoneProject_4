from django.test import TestCase
from .models import Product


class TestViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Product.objects.create(description='first product', friendly_name='product', price=100, brand='some')
        Product.objects.create(description='second product', friendly_name='product', price=200, brand='some')
    
    def test_get_products_page(self):
        response = self.client.get('/products/') # This is the top level URL define in project admin
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_product_detail_page(self):
        product = Product.objects.get(pk=1)
        response = self.client.get(f'/products/{product.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_sorting_by_price_asc(self):
        response = self.client.get('/products/', {'sort': 'price', 'ordering': 'asc'})
        self.assertEqual(response.status_code, 200)
        sorting = response.context['current_sorting']
        self.assertEqual(sorting, 'price_asc')
        self.assertTemplateUsed(response, 'products/products.html')

    def test_sorting_by_price_desc(self):
        response = self.client.get('/products/', {'sort': 'price', 'ordering': 'desc'})
        self.assertEqual(response.status_code, 200)
        sorting = response.context['current_sorting']
        self.assertEqual(sorting, 'price_desc')
        self.assertTemplateUsed(response, 'products/products.html')

    def test_sorting_by_price_asc(self):
        response = self.client.get('/products/', {'sort': 'price', 'ordering': 'asc'})
        self.assertEqual(response.status_code, 200)
        sorting = response.context['current_sorting']
        self.assertEqual(sorting, 'price_asc')
        self.assertTemplateUsed(response, 'products/products.html')

    def test_sorting_by_category_desc(self):
        response = self.client.get('/products/', {'sort': 'category', 'ordering': 'desc'})
        self.assertEqual(response.status_code, 200)
        sorting = response.context['current_sorting']
        self.assertEqual(sorting, 'category_desc')
        self.assertTemplateUsed(response, 'products/products.html')

    def test_sorting_by_category_asc(self):
        response = self.client.get('/products/', {'sort': 'category', 'ordering': 'asc'})
        self.assertEqual(response.status_code, 200)
        sorting = response.context['current_sorting']
        self.assertEqual(sorting, 'category_asc')
        self.assertTemplateUsed(response, 'products/products.html')

    def test_sorting_by_name_asc(self):
        response = self.client.get('/products/', {'sort': 'friendly_name', 'ordering': 'asc'})
        self.assertEqual(response.status_code, 200)
        sorting = response.context['current_sorting']
        self.assertEqual(sorting, 'friendly_name_asc')
        self.assertTemplateUsed(response, 'products/products.html')

    def test_sorting_by_name_desc(self):
        response = self.client.get('/products/', {'sort': 'friendly_name', 'ordering': 'desc'})
        self.assertEqual(response.status_code, 200)
        sorting = response.context['current_sorting']
        self.assertEqual(sorting, 'friendly_name_desc')
        self.assertTemplateUsed(response, 'products/products.html')