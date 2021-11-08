from django.shortcuts import render, redirect
from store.models import Product
from .models import Bag, BagItem
from django.http import HttpResponse


def view_bag(request):
    """ A view to see the contents of the shopping bag """
    return render(request, 'store/bag.html')


def _bag_id(request):
    """
    Bag ID will be the session ID for the Add to bag view,
    this is why this view will request the session ID.
    If there is none, this will create a session ID
    """
    bag = request.session.session_key
    if not bag:
        bag = request.session.create()
    return bag


def add_to_bag(request, product_id):
    """ 
    This view will add the product into the 
    shopping bag in the given quantity
    """
    product = Product.objects.get(id=product_id)
    try:
        # Get the Bag ID present in the session
        bag = Bag.objects.get(bag_id=_bag_id(request))
    except Bag.DoesNotExist:
        bag = Bag.objects.create(
            bag_id = _bag_id(request)
        )
    bag.save()

    try:
        bag_item = BagItem.objects.get(product=product, bag=bag)
        bag_item.quantity += 1
        bag_item.save()
    except BagItem.DoesNotExist:
        bag_item = BagItem.objects.create(
            product = product,
            quantity = 1,
            bag = bag,
        )
        bag_item.save()
    return HttpResponse(bag_item.product)
    exit()
    return redirect('bag')