from django.shortcuts import render, HttpResponse
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

def addAGuest (request):

    if request.method == 'POST':

        

        guest = Guest()
        guest.first_name = request.POST['fname']
        guest.last_name =request.POST['lname']
        guest.gov_id =request.POST['gov-id']
        guest.check_in_time =request.POST['checkin']
        guest.check_out =request.POST['checkout']
        current_room = request.POST['roomno']
        guest.room_number = Rooms.objects.get(room_no = current_room)
        guest.save()
        return HttpResponse ("added succesfully")
        
        # return render (request, 'addGuest.html')
    


    guest = Guest.objects.all()
    context = {
        'guests' : guest

    }
    return render(request, 'addGuest.html', context)
