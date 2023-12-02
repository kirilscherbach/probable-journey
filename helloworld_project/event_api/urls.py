from django.urls import path

from .views import (
    EventDetail,
    EventList,
    SongAtEventMappingDetail,
    SongAtEventMappingList,
)

urlpatterns = [
    path("event/", EventList.as_view()),
    path("event/<int:pk>/", EventDetail.as_view()),
    path("mapping/", SongAtEventMappingList.as_view()),
    path("mapping/<int:pk>/", SongAtEventMappingDetail.as_view()),
]
