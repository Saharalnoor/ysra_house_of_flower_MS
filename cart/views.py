from django.shortcuts import render, redirect, \
    reverse, HttpResponse, get_object_or_404
from products.models import Product
from django.contrib import messages

# Create your views here.


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the selected product/service to the cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """Update the quantity of the selected product/service in the cart
        to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    product = Product.objects.get(pk=item_id)
    cart = request.session.get('cart', {})
    datetime = None
    if 'datetime' in request.POST:
        datetime = request.POST['datetime']
    if datetime:
        if quantity > 0:
            cart[item_id] = {'items_by_datetime': {datetime: quantity}}
            messages.success(request,
                             (f'Successfully Updated {product.name}'))

    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'Updated {product.name}\
                quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the cart"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        request.session['cart'] = cart
        messages.warning(request, f'You removed \
                         {product.name} from your cart!')
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item from the cart: {e}')
        return HttpResponse(status=500)
