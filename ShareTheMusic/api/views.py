from django.shortcuts import render
from .models import Room
from .serializers import RoomSerializer
from rest_framework import generics
#urls will point to this func to display, urlsSTM -> urlsAPI -> views

#func will allow us to create and view the rooms for backend
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
