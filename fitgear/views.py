from django.shortcuts import render
from store.models import Product


def home(request):
    """ A view to return the Index page """
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products': products,
    }
    return render(request, 'home.html', context)


def contact(request):
    """ A view to return the Contact page """
    return render(request, 'contact.html')
