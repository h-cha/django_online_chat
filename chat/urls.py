# -*- coding: utf-8 -*-

from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
       # path('', views.index, name='index'),
        path('<str:room_name>/', views.room, name='room'),
        path('<str:room_name>/start', views.start, name='start'),
        path('<str:room_name>/vote', views.vote, name='vote'),
]