from django.urls import path, include
from hotelapp import views

urlpatterns = [
    
    path('', views.home , name="home"),
    path('showallguest', views.showallguest, name='showallguest'),
    path('addaguest', views.addAGuest, name="addaguest"),
    path('filterguest', views.filterGuest, name="filterguest"),
    path('delete_guest', views.delete_guest, name='delete_guest'),
    path('delete_guest/<int:gov_id>/', views.delete_guest, name='delete_guest'),
]