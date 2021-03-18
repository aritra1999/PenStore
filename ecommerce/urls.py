from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('auth/', include('accounts.urls')),
] 
