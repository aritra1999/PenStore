from django.contrib import admin
from django.urls import path, include

from .views import (
    dashboard_view,

)

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    # path('products', orders_placed_view, name='orderes_places')
]
