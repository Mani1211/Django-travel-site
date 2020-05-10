from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    reviews = CustomerReview.objects.all()
    tourtype = 'INTERNATIONAL'
    dests = Destinaion.objects.filter(tourtype=tourtype)
    print(dests)
    return render(request,'index.html',{'reviews':reviews,'dests':dests})

def about(request):
    reviews = CustomerReview.objects.all()
    return render(request,'about.html',{'reviews':reviews,})

def contact(request):
    return render(request,'contact.html')

def how(request):
    return render(request,'how.html')

def international(request):
    reviews = CustomerReview.objects.all()
    tourtype = 'INTERNATIONAL'
    dests = Destinaion.objects.filter(tourtype=tourtype)
    print(dests)
    return render(request,'index.html',{'reviews':reviews,'dests':dests})

def domestic(request):
    tourtype = 'DOMESTIC'
    reviews = CustomerReview.objects.all()
    dests = Destinaion.objects.filter(tourtype=tourtype)
    print(dests)
    return render(request,'index.html',{'reviews':reviews,'dests':dests})

def moreideas(request):
   
    reviews = CustomerReview.objects.all()
    dests = Destinaion.objects.all()
    print(dests)
    return render(request,'destination.html',{'reviews':reviews,'dests':dests})

def destmap(request,pk):
    destmap = Destinaion.objects.get(id = pk)
    print(destmap)
    return render(request,'map.html',{'destmap':destmap})