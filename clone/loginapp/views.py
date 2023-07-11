from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from . forms import NewUser


# Create your views here.
def home(request):
    return render(request, 'index.html')


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful, you are welcome')
                return redirect('http://127.0.0.1:8000/admin/')
            messages.error(request, 'Incorrect login details')

    form = AuthenticationForm()
    return render(request, 'login_user.html', {'form': form})
