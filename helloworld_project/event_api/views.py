from django.core.exceptions import PermissionDenied
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from .models import Event, EventAttendee, SongAtEventMapping
from .serializers import (
    EventAttendeeSerializer,
    EventSerializer,
    SongAtEventMappingSerializer,
)


class EventList(generics.ListCreateAPIView):
    serializer_class = EventSerializer

    def get_permissions(self):
        """
        Override to customize permission for different actions.
        """
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminUser()]

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


class EventAttendeeList(generics.ListCreateAPIView):
    serializer_class = EventAttendeeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = EventAttendee.objects.filter(
            event__event_organizer=self.request.user
        )
        return queryset

    def perform_create(self, serializer):
        if self.request.user != serializer.validated_data["event"].event_organizer:
            raise PermissionDenied("You are not the organizer of this event.")
        serializer.save()
