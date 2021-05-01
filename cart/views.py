from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_cart(request):
    """ A view to render cart.html template for the shopping cart page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add the quantity of selected product to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated {product.friendly_name} quantity to {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request, f'You have added {product.friendly_name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """Remove item from shopping cart"""

    product = get_object_or_404(Product, pk=item_id)
    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.success(request, f'You have removed {product.friendly_name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
