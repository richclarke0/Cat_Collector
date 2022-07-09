from django.shortcuts import render
from django.http import HttpResponse
from .models import Cat
from django.views.generic.edit import CreateView

# Add the Cat class & list and view function below the imports
# class Cat:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, breed, description, age):
#     self.name = name
#     self.breed = breed
#     self.description = description
#     self.age = age

# cats = [
#   Cat('Lolo', 'tabby', 'foul little demon', 3),
#   Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#   Cat('Raven', 'black tripod', '3 legged cat', 4)
# ]

# this is the new database import


# Create your views here.
#this is our controller file where we create all of our individual views

def home(request):
    return HttpResponse("<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>") #HttpResponse is like res.send in express

# def about(request):
#     return HttpResponse("about page") #aboutpage

#render a page instead!
def about(request):
  return render(request, 'about.html')

def cats_index(request):
# this is the new database importline
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats })

def cats_detail(request, cat_id):
  #get our individual cat
  cat = Cat.objects.get(id=cat_id)
  #render template, pass it to the cat
  return render(request, 'cats/detail.html', { 'cat': cat })

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'