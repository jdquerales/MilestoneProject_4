from django.test import TestCase
from .models import Category, Origin, Location

# Create your tests here.
class TestModels(TestCase):
# Set up non-modified objects used by all test methods
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(name='Test Category', friendly_name='Test friendly name')
        Origin.objects.create(name='Test Origin', friendly_name='Test Origin friendly name')
        Location.objects.create(name='Test Location', friendly_name='Test Location friendly name')
    
    def test_category_name_label(self):
        name = Category.objects.get(pk=1)
        field_label = name._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_category_friendly_name_label(self):
        name = Category.objects.get(pk=1)
        field_label = name._meta.get_field('friendly_name').verbose_name
        self.assertEqual(field_label, 'friendly name')

    def test_category_name_max_length(self):
        name = Category.objects.get(id=1)
        max_length = name._meta.get_field('name').max_length
        self.assertEqual(max_length, 254)

    def test_category_friendly_name_max_length(self):
        friendly_name = Category.objects.get(pk=1)
        max_length = friendly_name._meta.get_field('friendly_name').max_length
        self.assertEqual(max_length, 254)

    def test_category_string_method(self):
        item = Category.objects.get(pk=1)
        expected_object_name = f'{item.name}'
        self.assertEqual(expected_object_name, str(item))

    def test_origin_name_label(self):
        name = Origin.objects.get(pk=1)
        field_label = name._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_origin_friendly_name_label(self):
        name = Origin.objects.get(pk=1)
        field_label = name._meta.get_field('friendly_name').verbose_name
        self.assertEqual(field_label, 'friendly name')

    def test_origin_name_max_length(self):
        name = Origin.objects.get(id=1)
        max_length = name._meta.get_field('name').max_length
        self.assertEqual(max_length, 254)

    def test_origin_friendly_name_max_length(self):
        friendly_name = Origin.objects.get(pk=1)
        max_length = friendly_name._meta.get_field('friendly_name').max_length
        self.assertEqual(max_length, 254)

    def test_origin_string_method(self):
        item = Origin.objects.get(pk=1)
        expected_object_name = f'{item.name}'
        self.assertEqual(expected_object_name, str(item))

    def test_location_name_label(self):
        name = Location.objects.get(pk=1)
        field_label = name._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_location_friendly_name_label(self):
        name = Location.objects.get(pk=1)
        field_label = name._meta.get_field('friendly_name').verbose_name
        self.assertEqual(field_label, 'friendly name')

    def test_location_name_max_length(self):
        name = Location.objects.get(id=1)
        max_length = name._meta.get_field('name').max_length
        self.assertEqual(max_length, 254)

    def test_location_friendly_name_max_length(self):
        friendly_name = Location.objects.get(pk=1)
        max_length = friendly_name._meta.get_field('friendly_name').max_length
        self.assertEqual(max_length, 254)

    def test_location_string_method(self):
        item = Location.objects.get(pk=1)
        expected_object_name = f'{item.name}'
        self.assertEqual(expected_object_name, str(item))
