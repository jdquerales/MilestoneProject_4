from django.test import TestCase
from .models import Category

# Create your tests here.
class TestModels(TestCase):
# Set up non-modified objects used by all test methods
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(name='Test Category', friendly_name='Test friendly name')
    
    def test_name_label(self):
        name = Category.objects.get(pk=1)
        field_label = name._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_friendly_name_label(self):
        name = Category.objects.get(pk=1)
        field_label = name._meta.get_field('friendly_name').verbose_name
        self.assertEqual(field_label, 'friendly name')

    def test_name_max_length(self):
        name = Category.objects.get(id=1)
        max_length = name._meta.get_field('name').max_length
        self.assertEqual(max_length, 254)

    def test_friendly_name_max_length(self):
        friendly_name = Category.objects.get(pk=1)
        max_length = friendly_name._meta.get_field('friendly_name').max_length
        self.assertEqual(max_length, 254)

    def test_string_method(self):
        item = Category.objects.get(pk=1)
        expected_object_name = f'{item.name}'
        self.assertEqual(expected_object_name, str(item))

