from django.shortcuts import render, redirect
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from bag.models import Bag, BagItem
from .models import Order, OrderProduct, Payment
from bag.views import _bag_id
from .forms import OrderForm
import uuid
import datetime
import stripe
import json


@login_required(login_url='login')
def checkout(request, total=0, quantity=0, bag_items=None):
    """
    This view will process the checkout functionality.
    User can order and pay for the products in the basket.
    Stripe payment system integrated.
     """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    intent = None

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
    if request.method == 'POST':
        if request.user.is_authenticated:
            bag, created = Bag.objects.get_or_create(bag_id=_bag_id(request))
            bag_items = BagItem.objects.filter(
                user=request.user, is_active=True)
        else:
            bag, created = Bag.objects.get_or_create(bag_id=_bag_id(request))
            bag_items = BagItem.objects.filter(bag=bag, is_active=True)

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

        # Generate order number
        order_number = uuid.uuid4().hex.upper()

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.user = request.user
            order.original_bag = bag
            order.order_total = grand_total
            order.tax = tax
            order.order_number = order_number
            order.save()

            for bag_item in bag_items:
                order_product = OrderProduct.objects.create(
                    user=request.user,
                    order=order,
                    product=bag_item.product,
                    quantity=bag_item.quantity,
                    product_price=bag_item.product.price,
                    ordered=True,
                )
                order_product.variations.set(bag_item.variations.all())
                order_product.save()

            # Updating Payment Table
            new_Payment = Payment(
                user=request.user,
                payment_id=order.order_number,
                payment_method="Stripe",
                amount_paid=grand_total,
                status="Complete"
            )
            new_Payment.save()

            order.is_ordered = True
            order.payment = new_Payment
            order.save()
            return redirect(reverse('success', args=(order_number,)))

    else:
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


def success(request, order_id):
    """"
    Once payment has been completed, user is directed
    to an order confirmation page
    """
    # Clear Bag
    BagItem.objects.filter(user=request.user).delete()
    main_order = Order.objects.get(order_number=order_id)
    ordered_product = OrderProduct.objects.filter(order=main_order)
    total_price = main_order.order_total - main_order.tax
    context = {
        "order": ordered_product,
        "main_order": main_order,
        "total_price": total_price,
    }
    return render(request, 'checkout/checkout-success.html', context=context)
