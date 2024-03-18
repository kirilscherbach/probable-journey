from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchQuery, SearchRank
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from song_api.models import Song

from .models import Event, EventAttendee, SongAtEventMapping
from .serializers import (
    EventAttendeeSerializer,
    EventSerializer,
    SongAtEventMappingSerializer,
)


class EventPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        event_id = self.kwargs.get("event_id")
        event = get_object_or_404(Event, id=event_id)

        if user.is_superuser:
            return True
        if event.event_organizer == user:
            return True
        if EventAttendee.objects.filter(event=event, attendee=user.id).exists():
            return True

        return False


class EventAPI(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

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
        event_name = self.request.query_params.get("event_name")
        date = self.request.query_params.get("date")

        if organizer is not None:
            queryset = queryset.filter(event_organizer=organizer)
        if event_name is not None:
            queryset = queryset.filter(event_name__icontains=event_name)
        if date is not None:
            queryset = queryset.filter(date=date)

        return queryset


class EventDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = [IsAuthenticated]


class SongAtEventMappingAPI(generics.ListCreateAPIView):
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

    def create(self, request, *args, **kwargs):
        event_id = request.data.get("event")
        mapper_id = request.data.get("mapper")
        songs = request.data.get("songs")

        if not event_id or not mapper_id or not songs:
            return Response(
                {"detail": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST
            )

        event = get_object_or_404(Event, id=event_id)
        mapper = get_object_or_404(User, id=mapper_id)

        for song_id in songs:
            song = get_object_or_404(Song, id=song_id)
            SongAtEventMapping.objects.create(event=event, mapper=mapper, song=song)

        return Response(
            {"detail": "Mappings created successfully"}, status=status.HTTP_201_CREATED
        )


class SongAtEventMappingDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SongAtEventMappingSerializer
    queryset = SongAtEventMapping.objects.all()
    permission_classes = [IsAuthenticated]


class EventAttendeeAPI(EventPermissionMixin, generics.ListCreateAPIView):
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


class EventSongsView(LoginRequiredMixin, ListView):
    model = Song
    template_name = "event_api/song_mapper.html"
    context_object_name = "songs"

    def get_queryset(self, song_catalog_id):
        query = self.request.GET.get("q", "")
        if query:
            search_query = SearchQuery(query)
            return (
                Song.objects.annotate(rank=SearchRank("search_vector", search_query))
                .filter(search_vector=search_query, song_catalog=song_catalog_id)
                .order_by("-rank")
            )
        else:
            return Song.objects.filter(song_catalog=song_catalog_id)

    def get(self, request, *args, **kwargs):
        event_id = kwargs.get("event_id")
        event = get_object_or_404(Event, id=event_id)

        songs = self.get_queryset(event.song_catalog)

        song_mappings = SongAtEventMapping.objects.filter(event=event)
        song_mapper_dict = {
            mapping.song_id: (mapping.mapper_id, mapping.id)
            for mapping in song_mappings
        }

        for song in songs:
            if song.id in song_mapper_dict:
                song.is_selected = True
                if song_mapper_dict[song.id][0] == request.user.id:
                    song.can_delete = True
                    song.mapping_id = song_mapper_dict[song.id][1]
            else:
                song.is_selected = False
                song.can_delete = False

        return render(request, self.template_name, {"event": event, "songs": songs})


class EventView(LoginRequiredMixin, ListView):
    model = Event
    template_name = "event_api/events.html"
    context_object_name = "events"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get(self, request, *args, **kwargs):
        events = self.get_queryset()
        for event in events:
            if event.event_organizer == request.user:
                event.can_delete = True

        return render(
            request, self.template_name, {"events": events, "user": request.user}
        )
