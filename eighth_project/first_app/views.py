from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.RegistrationForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account created successfully')
                form.save()
                print(form.cleaned_data)
                
        else:
            form = forms.RegistrationForm()
            
        return render(request, './signup.html', {'form' : form})
    
    else:
        return redirect('profile')

def home(request):
    return render(request, './home.html')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                # check kortechi user database e ache kina
                user = authenticate(username=name, password=userpass)
                if user is not None:
                    login(request, user)
                    return redirect('profile')  # profile page e redirect korbe
                
        else:
            form = AuthenticationForm()
        return render(request, './login.html', {'form': form})
    
    else:
        return redirect('profile')


def profile(request):
    if request.user.is_authenticated: 
        return render(request, './profile.html', {'user': request.user})
    else:
        return redirect('login')

def user_logout(request):
    logout(request)
    return redirect('login')

