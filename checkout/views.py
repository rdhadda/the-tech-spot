from django.shortcuts import render, redirect, reverse
from .forms import OrderForm
from django.contrib import messages


def checkout(request):
    bag = request.session.get('bag', {})

    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PnKUSRoi0sqgpoHt1cNIV6DjnJJtN01h9yG1HAaZysW5XTeVwG7RBHH5hdjPOfQaEBIEl5z7Z6WUqBHKJwT3hcH00BxetiOX0',
        'client_secret': 'test client secret'
        
    }

    return render(request, template, context )