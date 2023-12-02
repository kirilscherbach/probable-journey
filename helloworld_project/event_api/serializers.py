from rest_framework import serializers

from .models import Event, SongAtEventMapping


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class SongAtEventMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongAtEventMapping
        fields = "__all__"
