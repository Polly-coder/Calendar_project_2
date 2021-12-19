from typing import Generic
from django.shortcuts import render
from rest_framework import generics
from meetme.serializers import EventDetailSerializer, EventsListSerializer, SlotDetailSerializer, SlotsListSerializer
from meetme.models import Event, Slot
from meetme.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.http import HttpResponse
import requests

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

class SlotCreateView(generics.CreateAPIView):
    serializer_class = SlotDetailSerializer

class SlotsListView(generics.ListAPIView):
    serializer_class = SlotsListSerializer
    queryset = Slot.objects.all()
    permission_classes = (IsAuthenticated, )


def mainPage(request):
    return render(request, 'main.html', {})

