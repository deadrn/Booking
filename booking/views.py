from django.shortcuts import render
from .models import Category, Room, Booking

def rooms_list(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'booking/rooms_list.html', context)