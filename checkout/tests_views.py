from django.test import TestCase


class TestViews(TestCase):

    def test_get_checkout_page(self):
        # This is the top level URL define in project admin
        response = self.client.get('/checkout/')
        self.assertRedirects(response, '/products/')