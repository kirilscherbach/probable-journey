from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Event, SongAtEventMapping
from .serializers import EventSerializer, SongAtEventMappingSerializer


class EventList(generics.ListCreateAPIView):
    serializer_class = EventSerializer

    def get_permissions(self):
        """
        Override to customize permission for different actions.
        """
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_queryset(self):
        queryset = Event.objects.all()
        organizer = self.request.query_params.get("organizer")
        if organizer is not None:
            queryset = queryset.filter(event_organizer=organizer)
        return queryset


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = [IsAuthenticated]


class SongAtEventMappingList(generics.ListCreateAPIView):
    serializer_class = SongAtEventMappingSerializer

    def get_permissions(self):
        """
        Override to customize permission for different actions.
        """
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_queryset(self):
        queryset = SongAtEventMapping.objects.all()
        event = self.request.query_params.get("event")
        if event is not None:
            queryset = queryset.filter(event=event)
        return queryset


class SongAtEventMappingDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SongAtEventMappingSerializer
    queryset = SongAtEventMapping.objects.all()
    permission_classes = [IsAuthenticated]
