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

    def test_user_field_instance(self):
        profile = UserProfile.objects.get(pk=1)
        self.assertIsInstance(profile.user, User)

    def test_default_phone_number_label(self):
        phone = UserProfile.objects.get(pk=1)
        field_label = phone._meta.get_field('default_phone_number').verbose_name
        self.assertEqual(field_label, 'default phone number')

    def test_default_street_address1_label(self):
        address1 = UserProfile.objects.get(pk=1)
        field_label = address1._meta.get_field('default_street_address1').verbose_name
        self.assertEqual(field_label, 'default street address1')

    def test_default_street_address2_label(self):
        address2 = UserProfile.objects.get(pk=1)
        field_label = address2._meta.get_field('default_street_address2').verbose_name
        self.assertEqual(field_label, 'default street address2')

    def test_default_town_or_city_label(self):
        city = UserProfile.objects.get(pk=1)
        field_label = city._meta.get_field('default_town_or_city').verbose_name
        self.assertEqual(field_label, 'default town or city')

    def test_profile_string_method(self):
        profile = UserProfile.objects.get(pk=1)
        user = User.objects.get(pk=1)
        expected_object_name = f'{user.username}'
        self.assertEqual(expected_object_name, str(user))

    def test_product_phone_number_max_length(self):
        profile = UserProfile.objects.get(pk=1)
        max_length = profile._meta.get_field('default_phone_number').max_length
        self.assertEqual(max_length, 20)