from django import forms

class CouponApplyForm(form.Form):
    code = forms.CharField()