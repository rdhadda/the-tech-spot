from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ View show the contents of the shoppers bag """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ View to allow users to add products to their bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)