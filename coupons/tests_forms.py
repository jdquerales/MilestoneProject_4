from django.test import TestCase
from .forms import CouponApplyForm

class TestCouponApplyForm(TestCase):

    def test_code_is_required(self):
        form = CouponApplyForm({'code': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('code', form.errors.keys())
        self.assertEqual(form.errors['code'][0], 'This field is required.')

