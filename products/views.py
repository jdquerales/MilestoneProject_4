from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from django.db.models.functions import Lower

# Create your views here.


def all_products(request):
    """ A view to display all products on screen, and it also include queries"""

    products = Product.objects.all()  # This method will return all products from the
    query = None
    categories = None
    sort = None
    ordering = None
    limit = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'friendly_name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('friendly_name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'ordering' in request.GET:
                ordering = request.GET['ordering']
                if ordering == 'desc':
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('home'))
            queries = Q(friendly_name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{ordering}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to retrieve a particular product by its id"""
    product = get_object_or_404(Product, pk=product_id)
    # to get a particular product by id

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
