from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from products.models import Product
from django.contrib import messages
# Create your views here.

def view_bag(request):
    """ View show the contents of the shoppers bag """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ View to allow users to add products to their bag """

    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """Adjust the quantity of products within the bag"""

    quantity = int(request.POST.get('quantity'))
    

    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity        
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """
    Remove product from bag
    """

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        
        return HttpResponse(status=500)
