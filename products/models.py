from django.db import models
from profiles.models import UserProfile
from django.contrib.auth.models import User

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Origin(models.Model):
    class Meta:
        verbose_name_plural = 'Origins'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Location(models.Model):
    class Meta:
        verbose_name_plural = 'Locations'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    class Meta:
        verbose_name_plural = 'Products'

    description = models.TextField()
    friendly_name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    body_location= models.ForeignKey('Location', null=True, blank=True, on_delete=models.SET_NULL)
    brand = models.CharField(max_length=254, null=True, blank=True)
    origin = models.ForeignKey('Origin', null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(null=True, blank=True)
    stock = models.BooleanField(null=False, blank=True, default=True)
    user_wishlist = models.ManyToManyField(User, related_name="user_wishlist", blank=True)

    def __str__(self):
        return self.friendly_name

    def get_friendly_name(self):
        return self.friendly_name