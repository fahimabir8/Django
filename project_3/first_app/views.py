from django.shortcuts import render

# Create your views here.
def home(request):
    d = {'author': 'jelly', 'age':9, 'list' : [2,3,4]}
    return render(request,'home.html',d)