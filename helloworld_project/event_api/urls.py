from django.urls import path

from .views import (
    EventAPI,
    EventAttendeeAPI,
    EventDetailAPI,
    EventSongsView,
    EventView,
    SongAtEventMappingAPI,
    SongAtEventMappingDetailAPI,
)

urlpatterns = [
    path("events/", EventAPI.as_view(), name="events"),
    path("events/<int:pk>/", EventDetailAPI.as_view(), name="events_detail"),
    path("mappings/", SongAtEventMappingAPI.as_view(), name="mappings"),
    path(
        "mappings/<int:pk>/",
        SongAtEventMappingDetailAPI.as_view(),
        name="mappings_detail",
    ),
    path("event_attendees/", EventAttendeeAPI.as_view(), name="event_attendees"),
    path("event/<int:event_id>/songs/", EventSongsView.as_view(), name="event_songs"),
    path("event/list/", EventView.as_view(), name="event_list"),
]
