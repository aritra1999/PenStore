from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from .views import (
    signin_view,
    signup_view
)

urlpatterns = [
    path('signin/', signin_view, name='signin'),
    path('signup/', signup_view, name='signup'),
    path('logout/', LogoutView.as_view(), name="logout"),
]
