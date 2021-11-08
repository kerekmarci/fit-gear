from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import Bag, BagItem
from django.http import HttpResponse


def view_bag(request, total=0, quantity=0, bag_items=None):
    """ A view to see the contents of the shopping bag """
    try:
        bag = Bag.objects.get(bag_id=_bag_id(request))
        bag_items = BagItem.objects.filter(bag=bag, is_active=True)
        for bag_item in bag_items:
            total += (bag_item.product.price * bag_item.quantity)
            quantity += bag_item.quantity
        tax = (5 * total) / 100
        grand_total = total + tax
    except ObjectNotExist:
            pass

    context = {
        'total': total,
        'quantity': quantity,
        'bag_items': bag_items,
        'tax': tax,
        'grand_total': grand_total,
    }
    return render(request, 'store/bag.html', context)


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
    return redirect('bag')


def remove_from_bag(request, product_id):
    """ 
    This view will remove the product from the 
    shopping bag in the given quantity
    """
    bag = Bag.objects.get(bag_id=_bag_id(request))
    product = get_object_or_404(Product, id=product_id)
    bag_item = BagItem.objects.get(product=product, bag=bag)
    if bag_item.quantity > 1:
        bag_item.quantity -= 1
        bag_item.save()
    else:
        bag_item.delete()
    return redirect('bag')