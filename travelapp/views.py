from django.http import HttpResponse
from django.shortcuts import render
from . models import Place,Team

def home(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})


def result(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    add=x+y
    mult=x*y
    div=x/y
    sub=x-y
    return render(request,'result.html',{'add':add,'mult':mult,'div':div,'sub':sub})