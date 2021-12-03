from typing import Generic
from django.shortcuts import render
from rest_framework import generics
from meetme.serializers import EventDetailSerializer

# Create your views here.

class EventCreateView(generics.CreateAPIView):
    serializer_class = EventDetailSerializer