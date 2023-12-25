from django.urls import path

from .views import (
    EventAttendeeList,
    EventDetail,
    EventList,
    SongAtEventMappingDetail,
    SongAtEventMappingList,
)

urlpatterns = [
    path("events/", EventList.as_view()),
    path("events/<int:pk>/", EventDetail.as_view()),
    path("mappings/", SongAtEventMappingList.as_view()),
    path("mappings/<int:pk>/", SongAtEventMappingDetail.as_view()),
    path("event_attendees/", EventAttendeeList.as_view()),
]
