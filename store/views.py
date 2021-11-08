from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from bag.models import BagItem
from bag.views import _bag_id


def store(request, category_slug=None):
    """
    This view will display the products by category.
    """
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }

    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    """
    This view will display the individual products on a separate
    product detail page.
    """
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        # in_bag is to establish whether the item has already been added to the bag
        in_bag = BagItem.objects.filter(bag__bag_id=_bag_id(request), product=single_product).exists()
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
        'in_bag': in_bag,
    }
    return render(request, 'store/product_detail.html', context)