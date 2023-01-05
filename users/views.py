from django.shortcuts import render, redirect
from django.views import View
from users.forms import UserCreationForm, LoginForm
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# Create your views here.


class RegistrationView(View):

    def get(self, request):
        context = {'form': UserCreationForm()}
        return render(request, 'users/register.html', context)

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect(reverse('home'))
        context = {'form': form}
        return render(request, 'users/register.html', context)
    

class Login(View):
    
    def get(self, request):
        context = {'form': LoginForm()}
        return render(request, 'users/login.html', context)
    
    def post(self, request):
        form = LoginForm(request.POST, request=request)
        if form.is_valid():
            form.login_user()
            messages.success(request, 'Login successful')
            return redirect(reverse('home'))
        messages.success(request, 'Authentication failed')
        context = {'form': form}
        return render(request, 'users/login.html', context)
    
def logout_view(request):
    logout(request)
    messages.success(request, 'User logged out successfully')
    return redirect(reverse('users:login'))
    


    
