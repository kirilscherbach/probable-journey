from django.urls import path

from . import views

urlpatterns = [
    path("songs/", views.SongList.as_view(), name="song-list"),
    path("songs/<int:pk>/", views.SongUpdateDelete.as_view(), name="song-detail"),
    path("search/", views.SongSearchList.as_view(), name="song-search"),
    path("v-song-search/", views.SongSearchList.as_view(), name="v-song-search"),
    path("catalogs/", views.SongCatalogList.as_view(), name="song-catalog-list"),
    path(
        "catalogs/<int:pk>/",
        views.SongCatalogUpdateDelete.as_view(),
        name="song-catalog-detail",
    ),
]
