from django.shortcuts import render

from store.models import Product

def home_view(request):
    context = {
        'title': 'Home',
        'products': Product.objects.all().order_by('-timestamp')[0:4]
    }
    return render(request, 'store/home.html', context)


def store_view(request):
    context = {
        'title': 'Store',
        'products': Product.objects.all()
    }
    return render(request, 'store/store.html', context)


def cart_view(request):
    context = {
        'title': 'Cart'
    }
    return render(request, 'store/cart.html', context)


def checkout_view(request):
    context = {
        'title': 'Checkout'
    }
    return render(request, 'store/checkout.html', context)


def product_view(request, slug):
    product = ""
    try:
        product = Product.objects.get(slug=slug)
    except: 
        product = 'NULL'

    context = {
        'title': 'Product',
        'product': product
    }
    return render(request, 'store/product.html', context)


