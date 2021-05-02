from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile

class TestViews(TestCase):
# Set up non-modified objects used by all test methods
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(username='user_test')
        
    def test_username(self):
        user = User.objects.get(pk=1)
        self.assertEqual(user.username, 'user_test')

    def test_name_label(self):
        profile = UserProfile.objects.get(pk=1)
        self.assertIsInstance(profile.user, User)