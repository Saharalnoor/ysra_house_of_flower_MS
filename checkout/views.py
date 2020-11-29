from django.shortcuts import render, redirect, reverse
from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Hsd8OK4QpIUZwG9napIA3Ya6WVBXSlmaOstBTAhTsoCpDgDXtMSO9br3dvOwfC89eREdWqkVfNp5ibX9LqJSXCD00uDEeFPB1'
        'client_secret' 'test client secret',
    }

    return render(request, template, context)
