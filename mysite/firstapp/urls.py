from django.urls import path
from . import views

app_name="firstapp"

urlpatterns=[
    path("",views.index,name="index"),
    path("about",views.about,name="about"),
    path("info",views.about,name="info"),
        
]