from django.urls import path

from . import views

urlpatterns = [
    path("songs/", views.SongList.as_view(), name="song-list"),
    path("songs/<int:pk>/", views.SongUpdateDelete.as_view(), name="song-detail"),
    path("search/", views.SongSearchList.as_view(), name="song-search"),
]
