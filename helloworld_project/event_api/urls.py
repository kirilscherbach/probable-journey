from django.urls import path

from .views import (
    EventAttendeeList,
    EventDetail,
    EventList,
    EventSongsView,
    SongAtEventMappingDetail,
    SongAtEventMappingList,
)

urlpatterns = [
    path("events/", EventList.as_view(), name="events"),
    path("events/<int:pk>/", EventDetail.as_view(), name="events_detail"),
    path("mappings/", SongAtEventMappingList.as_view(), name="mappings"),
    path(
        "mappings/<int:pk>/", SongAtEventMappingDetail.as_view(), name="mappings_detail"
    ),
    path("event_attendees/", EventAttendeeList.as_view(), name="event_attendees"),
    path("event/<int:event_id>/songs/", EventSongsView.as_view(), name="event_songs"),
]
