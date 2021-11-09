from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product, Variation
from .models import Bag, BagItem
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse


def view_bag(request, total=0, quantity=0, bag_items=None):
    """ A view to see the contents of the shopping bag """
    try:
        tax = 0
        grand_total = 0
        bag = Bag.objects.get(bag_id=_bag_id(request))
        bag_items = BagItem.objects.filter(bag=bag, is_active=True)
        for bag_item in bag_items:
            total += (bag_item.product.price * bag_item.quantity)
            quantity += bag_item.quantity
        tax = (5 * total) / 100
        grand_total = total + tax
    except ObjectDoesNotExist:
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
    shopping bag in the given quantity, in the selected variation.
    """
    product = Product.objects.get(id=product_id)
    product_variation = []
    if request.method == 'POST':
        # This will store the category and value in key-value pairs,
        # for example color-white, size-medium;
        for item in request.POST:
            key = item
            value = request.POST[key]
            
            try:
                variation = Variation.objects.get(variation_category__iexact=key,
                    variation_value__iexact=value, product=product)
                product_variation.append(variation)
            except:
                pass
    
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
        if len(product_variation) > 0:
            bag_item.variations.clear()
            for item in product_variation:
                bag_item.variations.add(item)
        bag_item.quantity += 1
        bag_item.save()
    except BagItem.DoesNotExist:
        bag_item = BagItem.objects.create(
            product = product,
            quantity = 1,
            bag = bag,
        )
        if len(product_variation) > 0:
            bag_item.variations.clear()
            for item in product_variation:
                bag_item.variations.add(item)
        bag_item.save()
    return redirect('bag')


def remove_from_bag(request, product_id):
    """ 
    This view will decrease the product from the 
    shopping bag, or remove if the amount reaches 0
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


def remove_bag_item(request, product_id):
    """ 
    This view will act as a Delete Button to delete the product
    from the shopping bag, regardless of the quantity.
    """
    bag = Bag.objects.get(bag_id=_bag_id(request))
    product = get_object_or_404(Product, id=product_id)
    bag_item = BagItem.objects.get(product=product, bag=bag)
    bag_item.delete()
    return redirect('bag')