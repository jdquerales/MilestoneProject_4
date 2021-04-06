from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to display all products on screen, and it also include queries """

    products = Product.objects.all() # This method will return all products from the database

    context = {
        'products' : products,
    }

    return render(request, 'products/products.html', context)
