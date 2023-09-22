from django.urls import path, include
from hotelapp import views

urlpatterns = [
    
    path('', views.home , name="home")
]