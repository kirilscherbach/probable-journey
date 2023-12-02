from rest_framework import generics

from .models import Event, SongAtEventMapping
from .serializers import EventSerializer, SongAtEventMappingSerializer


class EventList(generics.ListCreateAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()
        organizer = self.request.query_params.get("organizer")
        if organizer is not None:
            queryset = queryset.filter(event_organizer=organizer)
        return queryset


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class SongAtEventMappingList(generics.ListCreateAPIView):
    serializer_class = SongAtEventMappingSerializer

    def get_queryset(self):
        queryset = SongAtEventMapping.objects.all()
        event = self.request.query_params.get("event")
        if event is not None:
            queryset = queryset.filter(event=event)
        return queryset


class SongAtEventMappingDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SongAtEventMappingSerializer
    queryset = SongAtEventMapping.objects.all()
