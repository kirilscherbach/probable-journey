from django.contrib.postgres.search import SearchQuery, SearchRank
from django.core.paginator import Paginator
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from .models import Song, SongCatalog
from .serializers import SongCatalogSerializer, SongSerializer


class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get_permissions(self):
        """
        Override to customize permission for different actions.
        """
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminUser()]


class SongUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAdminUser]


class SongSearchList(generics.ListAPIView):
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get("q", "")
        if query:
            search_query = SearchQuery(query)
            return (
                Song.objects.annotate(rank=SearchRank("search_vector", search_query))
                .filter(search_vector=search_query)
                .order_by("-rank")
            )
        else:
            return Song.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        paginator = Paginator(queryset, 10)  # Show 10 songs per page
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, "song_search.html", {"page_obj": page_obj})


class SongCatalogList(generics.ListCreateAPIView):
    queryset = SongCatalog.objects.all()
    serializer_class = SongCatalogSerializer

    def get_permissions(self):
        """
        Override to customize permission for different actions.
        """
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminUser()]


class SongCatalogUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = SongCatalog.objects.all()
    serializer_class = SongCatalogSerializer
    permission_classes = [IsAdminUser]
