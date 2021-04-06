from django.test import TestCase


class TestViews(TestCase):

    def test_get_products_page(self):
        response = self.client.get('/products/') # This is the top level URL define in project admin
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
