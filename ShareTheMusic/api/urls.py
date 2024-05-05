from django.urls import path,  
from .views import main

urlpatterns = [
    path('', main), #this links api url to the views.py which will run the main func in that app
]