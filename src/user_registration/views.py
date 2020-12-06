from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import logout


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout('/logout')
