from django.contrib import admin
from django.urls import path, include

from .views import (
    dashboard_view,
    add_product_view,
)

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('add_product', add_product_view, name='add_product'),

    # path('products', orders_placed_view, name='orderes_places')
]
