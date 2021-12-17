from django.db.models import fields
from rest_framework import serializers
from meetme.models import Event


class EventsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'date', 'user', 'guest')

class EventDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    class Meta:
        model = Event
        fields = '__all__'