from django.urls import path
from . import views,forms
urlpatterns = [
    path ('',views.home , name='homepage'),
   

]