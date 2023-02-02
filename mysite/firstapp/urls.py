from django.urls import path
from . import views

app_name="firstapp"

urlpatterns=[
    path("index",views.index,name="index"),
    path("about",views.about,name="about"),
    path("info",views.info,name="info"),
    path("",views.shoki,name="sho"),
  
]