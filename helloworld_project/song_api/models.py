from django.conf import settings
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVector, SearchVectorField
from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver


class SongCatalog(models.Model):
    song_catalog_name = models.CharField(max_length=250, unique=True)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    song_catalog_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.song_catalog_name} owned by {self.song_catalog_owner}"


class Song(models.Model):
    INTENSITY_CHOICES = [
        (0, "Intensity 0"),
        (1, "Intensity 1"),
        (2, "I'm too young to die"),
        (3, "Hey, not too rough"),
        (4, "Hurt me plenty"),
        (5, "Ultra-Violence"),
        (6, "Nightmare"),
    ]
    song_catalog = models.ForeignKey(SongCatalog, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    album = models.CharField(max_length=250, null=True, blank=True)
    genre = models.CharField(max_length=250, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    song_length = models.CharField(max_length=250, null=True, blank=True)
    charter = models.CharField(max_length=250, null=True, blank=True)
    intensity_guitar = models.IntegerField(
        choices=INTENSITY_CHOICES, null=True, blank=True
    )
    intensity_rhythm = models.IntegerField(
        choices=INTENSITY_CHOICES, null=True, blank=True
    )
    intensity_bass = models.IntegerField(
        choices=INTENSITY_CHOICES, null=True, blank=True
    )
    intensity_guitar_coop = models.IntegerField(
        choices=INTENSITY_CHOICES, null=True, blank=True
    )
    intensity_drums = models.IntegerField(
        choices=INTENSITY_CHOICES, null=True, blank=True
    )
    intensity_drums_real = models.IntegerField(
        choices=INTENSITY_CHOICES, null=True, blank=True
    )
    intensity_guitarghl = models.IntegerField(
        choices=INTENSITY_CHOICES, null=True, blank=True
    )
    intensity_bassghl = models.IntegerField(
        choices=INTENSITY_CHOICES, null=True, blank=True
    )
    intensity_rhythm_ghl = models.IntegerField(
        choices=INTENSITY_CHOICES, null=True, blank=True
    )
    intensity_guitar_coop_ghl = models.IntegerField(
        choices=INTENSITY_CHOICES, null=True, blank=True
    )
    intensity_keys = models.IntegerField(
        choices=INTENSITY_CHOICES, null=True, blank=True
    )
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    search_vector = SearchVectorField(null=True, blank=True)

    class Meta:
        indexes = [GinIndex(fields=["search_vector"])]

    def __str__(self):
        return f"Song by {self.artist}: {self.song_title}"


@receiver(post_save, sender=Song)
def update_search_vector(sender, instance, **kwargs):
    with transaction.atomic():
        Song.objects.filter(pk=instance.pk).update(
            search_vector=(
                SearchVector("artist", weight="A")
                + SearchVector("song_title", weight="A")
                + SearchVector("album", weight="B")
                + SearchVector("genre", weight="C")
            )
        )
