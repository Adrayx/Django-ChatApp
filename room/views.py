from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Room, Message
from .forms import RoomForm


# Create your views here.
@login_required
def rooms(request):
    allRooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': allRooms})


@login_required
def room(request, slug):
    requestedRoom = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=requestedRoom)[0:25]

    return render(request, 'room/room.html', {'room': requestedRoom, 'messages': messages})


@login_required
def create_room(request):
    if request.method == "POST":
        form = RoomForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('rooms')

    else:
        form = RoomForm()

    return render(request, 'room/create_room.html', {'form': form})
