from django.urls import path
from . import views #this is going to be our controller

urlpatterns = [ #this is a list of what our URLS are in our app
    #need to define our home route first
    path('', views.home, name='home')
]