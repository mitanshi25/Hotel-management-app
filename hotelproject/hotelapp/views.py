from django.shortcuts import get_object_or_404, render, HttpResponse
from hotelapp.models import Guest, Rooms
from django.db.models import Q

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
        # return HttpResponse ("added succesfully")
        
        return render (request, 'addGuest.html')
    


    guest = Guest.objects.all()
    context = {
        'guests' : guest

    }
    return render(request, 'addGuest.html', context)

def filterGuest(request):
    if request.method == "POST":

        guest = Guest()
        guest.first_name = request.POST['fname']
        guest.last_name = request.POST['lname']
        guest.gov_id = request.POST['gov-id']

        gues = Guest.objects.all()

        if guest.first_name:
            gues = gues.filter(Q(first_name__icontains=guest.first_name))

        if guest.last_name:
            gues = gues.filter(Q(last_name__icontains=guest.last_name))

        if guest.gov_id:
            gues = gues.filter(Q(gov_id=guest.gov_id))

        context = {

            'guests' : gues
        }

        return render(request, 'showallguest.html', context)
    
    if request.method == "GET":

        return render (request, 'filterGuest.html')


# def delete_guest(request, gov_id=0):
    # guest = get_object_or_404(Guest, gov_id=gov_id)
    # guest.delete()
    # if gov_id is not None:
    #     deleteGuest = Guest.objects.get(gov_id = gov_id)
    #     deleteGuest.delete()
    #     return HttpResponse("guest removed succesfully")
    # guest = Guest.objects.all()

    # context = {

    #     'guests' :guest
    # }

    # return render(request, "deleteguest.html", context)

def delete_guest(request, gov_id=None):
    if gov_id is not None:
        try:
            deleteGuest = Guest.objects.get(gov_id=gov_id)
        except Guest.DoesNotExist:
            return HttpResponse("Guest not found.")
        else:
            deleteGuest.delete()
            return HttpResponse("Guest removed successfully")

    guests = Guest.objects.all()

    context = {
        'guests': guests
    }

    return render(request, "deleteguest.html", context)