from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class userDetails(models.Model):
    
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    mobile = models.CharField(unique = True,max_length=256)
    address = models.CharField(unique = True,max_length=256)
    admin = models.BooleanField(default=False)
    time = models.DateTimeField(default = timezone.now())

    
class Grid(models.Model):
    grid1 = models.FloatField(unique = False,max_length=256)
    grid2 = models.FloatField(unique = False,max_length=256)
    grid3 = models.FloatField(unique = False,max_length=256)
    grid4 = models.FloatField(unique = False,max_length=256)
    time = models.DateTimeField(default = timezone.now())
    
    
class weather(models.Model):
    humidty = models.FloatField(unique = False,max_length=256)
    temperature = models.FloatField(unique = False,max_length=256)
    wind = models.FloatField(unique = False,max_length=256,default=0)
    time = models.DateTimeField(default = timezone.now())

    
class fieldParameter(models.Model):
    sunlight = models.FloatField(unique = False,max_length=256)
    rainfall = models.FloatField(unique = False,max_length=256)
    time = models.DateTimeField(default = timezone.now())


class Complain(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    complaintxn = models.CharField(max_length=256,default = "COMP123")
    complain = models.CharField(max_length=256)
    time = models.DateTimeField(default = timezone.now())
    complainid = models.CharField(max_length=256) 
    status = models.BooleanField(default=0)
    username = models.CharField(max_length=256,default="USER1")

    def __str__(self):
        return self.complain     
