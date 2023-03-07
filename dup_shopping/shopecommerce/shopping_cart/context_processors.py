from .models import CartItem, Cart_Cart
from .views import cart_id


def Counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart_Cart.objects.filter(cart_id=cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                item_count += cart_item.quantity
        except Cart_Cart.DoesNotExist:
            item_count = 0
    return dict(item_count=item_count)
