from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to display all products on screen, and it also include queries"""

    products = Product.objects.all()  # This method will return all products from the
    query = None

    if request.GET:
        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            queries = Q(friendly_name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)
