from clonehero_api.models import Song
from django.conf import settings
from django.db import models


class Event(models.Model):
    event_name = models.CharField(max_length=250, unique=True)
    event_date = models.DateField()
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    event_organizer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE  # new
    )

    def __str__(self) -> str:
        return f"{self.event_name} at {self.event_date}"


class EventPlan(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["event", "song"], name="unique_song_per_event"
            )
        ]

    def __str__(self) -> str:
        return f"{self.song.song_title} ({self.song.artist}) played at {self.event.event_name} event"
