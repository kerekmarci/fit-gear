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


def handler404(request, exception):
    """ A view for custom 404 error page """
    return render(request, '404.html', status=404)


def handler500(request):
    """ A view for custom 500 error page """
    return render(request, '500.html', status=500)


def handler403(request, exception):
    """ A view for custom 403 error page """
    return render(request, '403.html', status=403)
