from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ View show the contents of the shoppers bag """
    return render(request, 'bag/bag.html')