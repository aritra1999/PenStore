from django.shortcuts import render


def home_view(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'store/home.html', context)


def store_view(request):
    context = {
        'title': 'Store'
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
    context = {
        'title': 'Product'
    }
    return render(request, 'store/product.html', context)


