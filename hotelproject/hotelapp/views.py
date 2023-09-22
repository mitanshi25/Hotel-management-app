from django.shortcuts import render
from hotelapp.models import Guest, Rooms

# Create your views here.

def home (request):
    return render(request, 'home.html')
    
def showallguest (request):
    guest = Guest.objects.all()
    context = {
        'guests' : guest

    }
    return render(request, 'showallguest.html', context)