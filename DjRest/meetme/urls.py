from django.contrib import admin
from django.urls import path, include


from meetme.views import EventCreateView, EventsListView, EventDetailView, SlotCreateView, SlotsListView

urlpatterns = [
    path('event/create/', EventCreateView.as_view()),
    path('slot/create/', SlotCreateView.as_view()),
    path('all/', EventsListView.as_view()),
    path('event/detail/<int:pk>/', EventDetailView.as_view())
]