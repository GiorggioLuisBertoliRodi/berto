from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from .forms import registroForm, loginForm

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = registroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = registroForm()
    return render(request, 'usuarios/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = loginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = loginForm()
    return render(request, 'usuarios/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
