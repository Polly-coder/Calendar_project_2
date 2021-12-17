from typing import Generic
from django.shortcuts import render
from rest_framework import generics
from meetme.serializers import EventDetailSerializer, EventsListSerializer
from meetme.models import Event
from meetme.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.

class EventCreateView(generics.CreateAPIView):
    serializer_class = EventDetailSerializer

class EventsListView(generics.ListAPIView):
    serializer_class = EventsListSerializer
    queryset = Event.objects.all()
    permission_classes = (IsAuthenticated, )

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventDetailSerializer
    queryset = Event.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )