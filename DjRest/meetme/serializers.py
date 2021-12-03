from django.db.models import fields
from rest_framework import serializers
from meetme.models import Event

class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'