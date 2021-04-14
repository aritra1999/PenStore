from django.contrib import admin
from django.urls import path, include

from .views import (
    store_view,
    cart_view,
    checkout_view,
    product_view,
    home_view
)

urlpatterns = [
    path('', home_view, name='home'),
    path('store', store_view, name='store'),
    path('store/<slug>', product_view, name='product'),
    path('cart', cart_view, name='cart'),
    path('checkout', checkout_view, name='checkout'),
]
