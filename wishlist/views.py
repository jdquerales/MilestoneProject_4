from django.shortcuts import render,  get_object_or_404
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# Create your views here.

@login_required
def add_to_wishlist(request, item_id):
    product = get_object_or_404(Product, id=item_id)
    if product.user_wishlist.filter(id = request.user.id).exists():
        product.user_wishlist.remove(request.user)
        messages.success(request, product.friendly_name + " has been removed from your WishList")
    else:
        product.user_wishlist.add(request.user)
        messages.success(request, "Added " + product.friendly_name + " to your WishList")
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
