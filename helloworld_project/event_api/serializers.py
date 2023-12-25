from rest_framework import serializers

from .models import Event, EventAttendee, SongAtEventMapping


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class SongAtEventMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongAtEventMapping
        fields = "__all__"


class EventAttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAttendee
        fields = "__all__"
