from django.contrib import admin
from .models import Product, Category, Origin, Location, Review

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Origin)
admin.site.register(Location)
admin.site.register(Review)