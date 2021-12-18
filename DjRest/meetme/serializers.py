from django.db.models import fields
from rest_framework import serializers
from meetme.models import Event, Slot


class EventsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'user', 'guest')

class EventDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    slots = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Event
        fields = '__all__'

class SlotsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = '__all__'

class SlotDetailSerializer(serializers.ModelSerializer):
    #event = serializers.ReadOnlyField()
    class Meta:
        model = Slot
        fields = '__all__'