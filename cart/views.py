from django.shortcuts import render

# Create your views here.

def view_cart(request):
    """ A view to render cart.html template for the shopping cart page """
    return render(request, 'cart/cart.html')
