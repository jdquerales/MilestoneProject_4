from django.shortcuts import render

# Create your views here.

def view_cart(request):
    """ A view to render cart.html template for the shopping cart page """
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add the quantity of selected product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')