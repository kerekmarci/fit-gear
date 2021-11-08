from django.shortcuts import render


def view_bag(request):
    """ A view to see the contents of the shopping bag """
    return render(request, 'store/bag.html')
