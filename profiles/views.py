from django.shortcuts import render
from products.models import Product

def profile(request):
    """Display the user's profile"""
    template = 'profiles/profile.html'
    

    wishlist = Product.objects.filter(user_wishlist=request.user)
    # Here I retrieve all products from user wishlist
    print(wishlist)

    context = {'wishlist': wishlist,}
    
    return render(request, template, context)
    