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


def payments(request):
    return render(request, 'checkout/payments.html')


def place_order(request, total=0, quantity=0):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    current_user = request.user
    bag_items = BagItem.objects.filter(user=current_user)
    bag_count = bag_items.count()
    if bag_count <= 0:
        return redirect ('store')

    grand_total = 0
    tax = 0
    for item in bag_items:
        total += (item.product.price * item.quantity)
        quantity += item.quantity
    tax = (5 * total) / 100
    grand_total = total + tax
    stripe_total = round(grand_total * 100)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.country = form.cleaned_data['country']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = grand_total
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            # Generating Order Number
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr,mt,dt)
            current_date = d.strftime("%Y%m%d") #20210305
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()

            # Stripe
            stripe.api_key = stripe_secret_key
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )

            print(intent)

            order = Order.objects.get(user=current_user, is_ordered=False, order_number=order_number)
            context = {
                'order': order,
                'bag_items': bag_items,
                'total': total,
                'tax': tax,
                'grand_total': grand_total,
                'stripe_public_key': stripe_public_key,
                'client_secret': intent.client_secret,
            }
            return render(request, 'checkout/payments.html', context)
    else:
        return redirect('checkout')


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
            order_form.save()
            return redirect(reverse('checkout_success', args=[order.order_number]))

    else:
        try:
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
        except ObjectDoesNotExist:
                pass

        order_form = OrderForm()
        
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