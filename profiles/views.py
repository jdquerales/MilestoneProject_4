from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from products.models import Product
from .models import UserProfile
from .forms import UserProfileForm

def profile(request):
    """Display the user's profile"""
    template = 'profiles/profile.html'

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
    
    
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    wishlist = Product.objects.filter(user_wishlist=request.user)
    # Here I retrieve all products from user wishlist
    print(wishlist)
    print(orders)

    context = {
        'profile': profile,
        'form': form,
        'wishlist': wishlist,
        'orders': orders}
    
    return render(request, template, context)
    