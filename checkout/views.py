from django.shortcuts import render, redirect
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from bag.models import Bag, BagItem
from .forms import OrderForm
from .models import Order
import datetime
import stripe
import json

"""
def payments(request):
    return render(request, 'checkout/payments.html')
"""


@login_required(login_url='login')
def checkout(request, total=0, quantity=0, bag_items=None):
    """ A view to process checkout functionality """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        if request.user.is_authenticated:
            bag_items = BagItem.objects.filter(user=request.user, is_active=True)    
        else:
            bag = Bag.objects.get(bag_id=_bag_id(request))
            bag_items = BagItem.objects.filter(bag=bag, is_active=True)
        for bag_item in bag_items:
            total += (bag_item.product.price * bag_item.quantity)
            quantity += bag_item.quantity
        
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'address_line_1': request.POST['address_line_1'],
            'address_line_2': request.POST['address_line_2'],
            'city': request.POST['city'],
            'country': request.POST['country'],
            'order_note': request.POST['order_note'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            return redirect('store')

    else:
        tax = 0
        grand_total = 0
        if request.user.is_authenticated:
            bag_items = BagItem.objects.filter(user=request.user, is_active=True)    
        else:
            bag = Bag.objects.get(bag_id=_bag_id(request))
            bag_items = BagItem.objects.filter(bag=bag, is_active=True)
        for bag_item in bag_items:
            total += (bag_item.product.price * bag_item.quantity)
            quantity += bag_item.quantity
        tax = (5 * total) / 100
        grand_total = total + tax
        
        stripe.api_key = stripe_secret_key
        stripe_total = round(grand_total * 100)
        intent = stripe.PaymentIntent.create(
                    amount=stripe_total,
                    currency=settings.STRIPE_CURRENCY,
                )

    context = {
        'total': total,
        'quantity': quantity,
        'bag_items': bag_items,
        'tax': tax,
        'grand_total': grand_total,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, 'store/checkout.html', context)