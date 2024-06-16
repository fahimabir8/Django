from . import views
from django.urls import path

urlpatterns = [
    path('about/',views.about),
    path('contact/',views.contact),
]
