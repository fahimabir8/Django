from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
#set password form --> doesn't need old password
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
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
    if  request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                form.save()
                print(form.cleaned_data)
                
        else:
            form = forms.ChangeUserData(instance=request.user)
            
        return render(request, './profile.html', {'form' : form})
    
    else:
        return redirect('signuppage')



def user_logout(request):
    logout(request)
    return redirect('login')

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data = request.POST)
            if form.is_valid():
                messages.success(request, 'Password changed successfully')   
                form.save()
                update_session_auth_hash(request, form.user) #pass update korbe
                
                return redirect('profile')
            
        else:
            form = PasswordChangeForm(user= request.user)
        return render(request, './passchange.html',{'form':form})
    else:
        return redirect('login')

def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SetPasswordForm(user=request.user, data = request.POST)
            if form.is_valid():
                messages.success(request, 'Password changed successfully')   
                form.save()
                update_session_auth_hash(request, form.user) #pass update korbe
                
                return redirect('profile')
            
        else:
            form = SetPasswordForm(user= request.user)
        return render(request, './passchange.html',{'form':form})
    else:
        return redirect('login')

