from django.contrib.postgres.search import SearchQuery, SearchRank
from rest_framework import generics

from .models import Song
from .serializers import SongSerializer


class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongSearchList(generics.ListAPIView):
    serializer_class = SongSerializer

    def get_queryset(self):
        query = self.request.query_params.get("q", "")
        search_query = SearchQuery(query)
        return (
            Song.objects.annotate(rank=SearchRank("search_vector", search_query))
            .filter(search_vector=search_query)
            .order_by("-rank")
        )
