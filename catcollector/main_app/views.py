from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#this is our controller file where we create all of our individual views

def home(request):
    return HttpResponse("<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>") #HttpResponse is like res.send in express

def about(request):
    return HttpResponse("about page") #aboutpage