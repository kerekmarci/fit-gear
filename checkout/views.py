from django.shortcuts import render


def place_order(request):
    current_user = request.user
    bag_items = BagItem.objects.filter(user=current_user)
    bag_count = bag_items.count()
    if bag_count <= 0:
        return redirect ('store')

    if request.method == 'POST':
        form = OrderForm(request.POST)