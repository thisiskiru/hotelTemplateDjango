import datetime
from django.db import models

from django.contrib.auth.models import AbstractUser

class Reservation(models.Model):
    guest = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
    ]
    CheckIn = models.CharField(default=datetime.datetime.now, max_length=30)
    CheckOut = models.CharField(default=datetime.datetime.now, max_length=30)
    NumeberOfGuest = models.CharField(choices=guest,default=1,max_length=15)
    NumeberOfRooms = models.CharField(choices=guest,default=1,max_length=15)
    Phone = models.CharField(default=1,max_length=15)
    Email = models.EmailField()
    Date= models.DateTimeField(default=datetime.datetime.now)
    class Meta:
        db_table = 'Reservation'

class User(AbstractUser):
    Phone = models.CharField(default=1,max_length=15)
    class Meta:
        db_table = 'User'

from django.contrib.auth import get_user_model
User = get_user_model()

class landingPage(models.Model):
    im1 = models.ImageField()
    im2 = models.ImageField()
    im3 = models.ImageField()