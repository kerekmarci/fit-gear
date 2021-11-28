from django.shortcuts import render
from store.models import Product

def home(request):
    """ A view to return the Index page """
    products = Product.objects.all().filter(is_available=True)
    print(products)
    context = {
        'products': products,
    }
    return render(request, 'home.html', context)