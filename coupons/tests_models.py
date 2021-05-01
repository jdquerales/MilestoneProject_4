from django.test import TestCase
from .models import Coupon
import datetime


class TestCouponModel(TestCase):
    # Set up non-modified objects used by all test methods
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_valid_from = datetime.date(2021, 7, 1)
        test_valid_to = datetime.date(2021, 10, 1)
        Coupon.objects.create(code='TestCoupon',
                              valid_from = test_valid_from, 
                              valid_to = test_valid_to, 
                              discount = 10,
                              active = True)

    def test_code_field(self):
        coupon = Coupon.objects.get(pk=1)
        field_label = coupon._meta.get_field('code').verbose_name
        self.assertEqual(field_label, 'code')

    def test_code_max_length(self):
        coupon = Coupon.objects.get(pk=1)
        max_length = coupon._meta.get_field('code').max_length
        self.assertEqual(max_length, 50)

    def test_active_field_is_boolean(self):
        coupon = Coupon.objects.get(pk=1)
        self.assertIsInstance(coupon.active, bool)

    def test_active_field_is_not_string(self):
        coupon = Coupon.objects.get(pk=1)
        self.assertNotIsInstance(coupon.active, str)

    def test_coupon_string_method(self):
        coupon = Coupon.objects.get(pk=1)
        expected_object_name = f'{coupon.code}'
        self.assertEqual(expected_object_name, str(coupon))

    def test_coupon_discount_is_integer(self):
        coupon = Coupon.objects.get(pk=1)
        self.assertIsInstance(coupon.discount, int)