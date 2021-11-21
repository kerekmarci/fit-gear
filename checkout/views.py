from django.shortcuts import render, redirect
from bag.models import BagItem
from .forms import OrderForm
from .models import Order
import datetime


def payments(request):
    return render(request, 'checkout/payments.html')


def place_order(request, total=0, quantity=0):
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

            order = Order.objects.get(user=current_user, is_ordered=False, order_number=order_number)
            context = {
                'order': order,
                'bag_items': bag_items,
                'total': total,
                'tax': tax,
                'grand_total': grand_total,
                'stripe_public_key': 'stripe_public_key',
                'client_secret': 'intent.client_secret',
            }
            return render(request, 'checkout/payments.html', context)
    else:
        return redirect('checkout')