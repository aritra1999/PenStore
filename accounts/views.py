from django.shortcuts import render

def signin_view(request):
    context = {
        'title': 'Sign In'
    }
    return render(request, 'accounts/signin.html', context)

def signup_view(request):
    context = {
        'title': 'Sign Up'
    }
    return render(request, 'accounts/signup.html', context)
