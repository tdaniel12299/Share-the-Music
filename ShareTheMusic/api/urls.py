from django.urls import path  
from .views import RoomView

urlpatterns = [
    path('room', RoomView.as_view()) #this links api url to the views.py which will run the roomview func in that app
]