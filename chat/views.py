from django.shortcuts import render
from .models import *


# Create your views here.
import json
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.urls import reverse



def index(request):

    return render(request, 'chat/index.html', {})


def room(request, room_name):
    
    '''
    json_str = request.body.decode("utf-8")
    text_data_json = json.loads(json_str)

    name = text_data_json['user']
    room = text_data_json['room_name']
    word = ''
   # count = request.POST.get("room_name")
   # user = request.POST.get({{user.username}})
    #word = forms.Intege(required=False)
    new_room = Room(room_name=room,user_name=name,word=word,user_count=0)
    new_room.save()
    
    template = loader.get_template('chat/room.html')
    context = {
       
        'room': room
    }
    return HttpResponse(template.render(context, request))
    '''
    new_room = Room(room_name=room_name,user_name='',word='',user_count=0)
    new_room.save()
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

