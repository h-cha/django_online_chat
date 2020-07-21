from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
            'room_name':room_name
    })
    
def start(request, room_name):

    return render(request, 'chat/start.html', {
            'room_name':room_name
    })
def vote(request, room_name):

    return render(request, 'chat/vote.html', {
            'room_name':room_name
    })

def vote1(request):
    return render(request, 'chat/vote.html', {})