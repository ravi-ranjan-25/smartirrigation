from django.shortcuts import render
from api.models import Grid,weather,fieldParameter,userDetails
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils import timezone
from django.http import JsonResponse
import random
# from .serializers import TaxSerializer
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

# Create your views here.


def addGridData(request):
    G1 = request.GET.get('g1')
    G2 = request.GET.get('g2')
    G3 = request.GET.get('g3')
    G4 = request.GET.get('g4')

    g = Grid(grid1=G1,grid2=G2,grid3=G3,grid4=G4,)
    g.save()

    return JsonResponse({'result':1})

def field(request):
    Sunlight = request.GET.get('sunlight')
    Rainfall = request.GET.get('rainfall')

    w = fieldParameter(sunlight=Sunlight,rainfall=Rainfall)
    w.save()

    return JsonResponse({'result':1})

def weatherData(request):
    Sunlight = request.GET.get('humidity')
    Rainfall = request.GET.get('temperature')

    w = weather(humidty=Sunlight,temperature=Rainfall)
    w.save()

    return JsonResponse({'result':1})

def gridCall(request):
    g = request.GET.get('grid')
    
    
    w = Grid.objects.latest('time')

    x = 0

    if(g == 'grid1'):
        x = w.grid1
    elif(g == 'grid2'):
        x = w.grid2
    elif(g == 'grid3'):
        x = w.grid3
    elif(g == 'grid4'):
        x = w.grid4
        

    if(x>50):
        
        return JsonResponse({'result':0})
    else:
        
        return JsonResponse({'result':1})




def gridCallSoftware(request):
    
    
    w = Grid.objects.latest('time')

    grid = ['grid1','grid2','grid3','grid4']
    list = []
    for g in grid:
        x = 0
        if(g == 'grid1'):
            x = w.grid1
        elif(g == 'grid2'):
            x = w.grid2
        elif(g == 'grid3'):
            x = w.grid3
        elif(g == 'grid4'):
            x = w.grid4
        
        
        if(x>80 and x<100):
            list.append({g:{'moisture':x,'result':'No water required'}})
        elif(x<79 and x>50):
            list.append({g:{'moisture':x,'result':'Moderate'}})
        else:
            list.append({g:{'moisture':x,'result':'Dry'}})

    return JsonResponse({'result':list})


def show(request):
    
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    grid = ['grid1','grid2','grid3','grid4']

    
    w = Grid.objects.all()

    for z in w:
        
        list1.append(z.grid1)
        list2.append(z.grid2)
        list3.append(z.grid3)
        list4.append(z.grid4)

    return JsonResponse({'grid1':list1,'grid2':list2,'grid3':list3,'grid4':list4})
                

def signup(request):
    userName = request.GET.get('username')
    eMail = request.GET.get('email')
    firstname = request.GET.get('firstname')
    lastname = request.GET.get('lastname')
    Password = request.GET.get('password')
    Mobile = request.GET.get('mobile')
    Address = request.GET.get('address')
    
    check = User.objects.filter(username = userName)
    checkEmail = User.objects.filter(email = eMail)
    checkHouse = userDetails.objects.filter(mobile=Mobile)
   
    if len(check) > 0:
        
            return JsonResponse({'result':0,'message':'Username already exist'})
    
    elif len(checkEmail) > 0:

            return JsonResponse({'result':0,'message':'Email address already exist'})


    elif len(checkHouse) > 0:
             return JsonResponse({'result':0,'message':'Mobile already registered'})
    else:
        
        user1 = User.objects.create_user(username = userName, email=eMail, password=Password, first_name = firstname , last_name = lastname)
        house_add = userDetails(mobile = Mobile,address=Address)
        house_add.user = user1
        house_add.save()

        
        # Return 1
        return JsonResponse({'result':1,'message':'success'})

def login(request):
    userName = request.GET.get('username')
    Password = request.GET.get('password')
    

    user1 = authenticate(username=userName, password=Password)
    
    if user1 is not None:
        house = userDetails.objects.get(user = user1)
        return JsonResponse({'result':1,'username':user1.username,'email':user1.email,'firstname':user1.first_name,
                                'lastname':user1.last_name,'mobile':house.mobile})
    
    else:
        return JsonResponse({'result':0,'message':'Incorrect username or password'})
