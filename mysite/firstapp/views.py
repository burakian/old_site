from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context={
        "name":"isara",
    }
    return render(request,"firstapp/index.html",context)

def about(request):
    return render(request,"firstapp/about.html")

def info(request):
    return render(request,"firstapp/info.html")
