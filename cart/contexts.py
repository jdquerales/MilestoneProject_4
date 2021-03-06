from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from coupons.models import Coupon

def cart_contents(request):

    discount = 0

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})
    coupon_id = request.session.get('coupon_id', {})

    if coupon_id:
        try:
            coupon = Coupon.objects.get(pk=coupon_id)
        except Coupon.DoesNotExist:
            pass

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'coupon_id': coupon_id
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else: 
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    if coupon_id:
        discount = (coupon.discount / Decimal(100))*total

    total_price_after_discount = delivery + total - discount

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'standard_delivery_percentage': settings.STANDARD_DELIVERY_PERCENTAGE,
        'grand_total': grand_total,
        'total_price_after_discount': total_price_after_discount,
        'discount' : discount
    }

    return context