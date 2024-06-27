from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully')
            messages.info(request, 'Welcome')
            messages.warning(request, 'This is warning')
            form.save()
            print(form.cleaned_data)
            
    
    else:
        form = forms.RegistrationForm()
        
    return render(request, 'home.html', {'form' : form})
