from django.db import models

from django.urls import reverse

# Create your models here.
#models is a parent class, and this models class has a bunch of functionality built in

#i want a class called Cat that inherits from models.Model
class Cat(models.Model):
    #in the class define each property as model attributes
    #this defines it as a string field
    name = models.CharField(max_length = 100)
    breed = models.CharField(max_length = 100)
    #text field
    description = models.TextField(max_length=250)
    #integer
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})