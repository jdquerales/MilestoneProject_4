from django.shortcuts import render, get_object_or_404
from products.models import Product
from .models import UserProfile

def profile(request):
    """Display the user's profile"""
    template = 'profiles/profile.html'
    
    profile = get_object_or_404(UserProfile, user=request.user)

    wishlist = Product.objects.filter(user_wishlist=request.user)
    # Here I retrieve all products from user wishlist
    print(wishlist)

    context = {
        'profile': profile,
        'wishlist': wishlist,}
    
    return render(request, template, context)
    