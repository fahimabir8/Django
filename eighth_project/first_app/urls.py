from django.urls import path
from . import views
urlpatterns = [
    path ('signup/',views.signup , name='signuppage'),
    path('',views.home, name='homepage'),
    path('profile/',views.profile, name='profile'),
    path('login/',views.user_login, name='login'),
    path('logout/',views.user_logout, name='logout'),
]