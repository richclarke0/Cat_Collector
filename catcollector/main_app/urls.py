from django.urls import path
from . import views #this is going to be our controller

urlpatterns = [ #this is a list of what our URLS are in our app
    #need to define our home route first. slash is implied in the ''
    path('', views.home, name='home'),
    #about view. no slash in front.
    path('about/', views.about, name='about'),

    #add another path to cats
    path('cats/', views.cats_index, name='cats'),

    #cat by id
    path('cats/<int:cat_id>/', views.cats_detail, name='detail'),

    #add new path for create
    path('cats/create/', views.CatCreate.as_view(), name='cats_create'),

    #add update delete
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),
]