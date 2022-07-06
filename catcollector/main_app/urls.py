from django.urls import path
from . import views #this is going to be our controller

urlpatterns = [ #this is a list of what our URLS are in our app
    #need to define our home route first. slash is implied in the ''
    path('', views.home, name='home'),
    #about view. no slash in front.
    path('about/', views.about, name='about'),

    #add another path to cats
    path('cats/', views.cats_index, name='cats')
]