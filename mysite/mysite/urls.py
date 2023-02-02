from django.shortcuts import render

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('firstapp/',include('firstapp.urls')),
    path('second/',include('firstapp.urls')),
    path('third/',include('firstapp.urls')),


    path('',include('firstapp.urls')),
]
