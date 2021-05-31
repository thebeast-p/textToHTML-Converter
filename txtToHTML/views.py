from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    return render (request,'Home.html')

def about(request):
    return render (request,'About.html')

def contact(request):
    return render (request,'Contact.html')

def convert(request):
    return render (request,'ConvertPage.html')

def converted(request):  
    Data1=data()
    style=["background-color:powderblue;","color:blue;","font-family:verdana;","text-shadow: 2px 2px #000000;"]

    Data1.Title=request.GET['titl']
    Data1.h1=request.GET['hd1']
    Data1.h2=request.GET['hd2']
    Data1.h3=request.GET['hd3']
    Data1.p1=request.GET['p1']
    Data1.p2=request.GET['p2']
    Data1.p3=request.GET['p3']
    Data1.h4=request.GET['hd4']
    Data1.h5=request.GET['hd5']
    Data1.h6=request.GET['hd6']
    Data1.image=request.GET['image']
    Data1.alt=request.GET['alt']
    a=int(request.GET['sd1'])
    Data1.s1=style[a-1]
    a=int(request.GET['sd2'])
    Data1.s2=style[a-1]
    a=int(request.GET['sd3'])
    Data1.s3=style[a-1]
    a=int(request.GET['sd4'])
    Data1.s4=style[a-1]
    a=int(request.GET['sd5'])
    Data1.s5=style[a-1]
    a=int(request.GET['sd6'])
    Data1.s6=style[a-1]
    return render (request,'Converted.html',{"x" : Data1})
