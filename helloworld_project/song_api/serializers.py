from rest_framework import serializers

from .models import Song, SongCatalog


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = [
            "id",
            "song_title",
            "artist",
            "album",
            "genre",
            "year",
            "song_length",
            "charter",
            "intensity_guitar",
            "intensity_rhythm",
            "intensity_bass",
            "intensity_guitar_coop",
            "intensity_drums",
            "intensity_drums_real",
            "intensity_guitarghl",
            "intensity_bassghl",
            "intensity_rhythm_ghl",
            "intensity_guitar_coop_ghl",
            "intensity_keys",
        ]


class SongCatalogSerializer(serializers.ModelSerializer):
    class MetaL:
        model = SongCatalog
        fields = [
            "id",
            "song_catalog_name",
            "song_catalog_owner",
        ]
