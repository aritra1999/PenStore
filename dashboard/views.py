from django.shortcuts import render, redirect

# Create your views here.
from store.models import Product

def dashboard_view(request):
    context = {
        'title': 'Dashboard'
    }
    return render(request, 'dashboard/dashboard.html', context)


def add_product_view(request):
    context = {
        'title': 'Add Product',
    }

    if request.method == "POST":
        Product.objects.create(
            brand = request.POST.get('brand'),
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            thumbnail = request.FILES['thumbnail'],
            color=request.POST.get('color'),
            price=request.POST.get('price'),
        )
        return redirect('/dashboard')
    return render(request, 'dashboard/add_product.html', context)
