from django.test import TestCase


class TestViews(TestCase):

    def test_get_profile_page(self):
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')