from django.shortcuts import render, redirect
from django.conf import settings
from django.shortcuts import redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def home(request):
    return render(request, "home.html") 

def contact(request):
    return render(request, "contact.html") 

def about(request):
    return render(request, "about.html") 

def service(request):
    return render(request, 'service.html')

def guide(request):
    return render(request, 'guide.html')

def my_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            remember_me = form.cleaned_data['remember_me']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                    return redirect('info:home')
                else:
                    request.session.set_expiry(1209600)
                    return redirect('info:home')
            else:
                return redirect('info:login')
        else:
            return redirect('info:signup')
    else:
        form = LoginForm()
        return render(request, "login.html", {'form': form})
    
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('info:home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})