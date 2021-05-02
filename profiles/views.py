from django.shortcuts import render
from products.models import Product

def profile(request):
    """Display the user's profile"""
    template = 'profiles/profile.html'
    

    products = Product.objects.filter(user_wishlist=request.user)
    # Here I retrieve all products from user wishlist
    print(products)

    context = {'products': products,}
    
    return render(request, template, context)
    