from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('about/',views.about, name='about'),
    path('form/',views.submit_form, name='submit_form'),
    path('django_form/',views.PasswordValidate, name='django_form')
]