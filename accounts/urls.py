# -*- coding: utf-8 -*-

from django.urls import path
from . import views

 
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('signup/', views.SignUp.as_view(), name='signup')
]