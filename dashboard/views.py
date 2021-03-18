from django.shortcuts import render

# Create your views here.

def dashboard_view(request):
    context = {
        'title': 'Dashboard'
    }
    return render(request, 'dashboard/dashboard.html', context)

