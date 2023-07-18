from django.db import models
from datetime import datetime

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15) 
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")

class Room(models.Model):
    name = models.CharField(max_length=50)
    user = models.CharField(max_length=100, default="")
    
class Message(models.Model):
    value = models.CharField(max_length=1000)
    created_at = models.DateTimeField(default = datetime.now, blank = True)
    user = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    