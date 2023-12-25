from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from song_api.models import Song, SongCatalog


class Event(models.Model):
    event_name = models.CharField(max_length=250, unique=True)
    event_date = models.DateField()
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    song_catalog = models.ForeignKey(SongCatalog, on_delete=models.CASCADE)
    event_organizer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.event_name} at {self.event_date}"


class SongAtEventMapping(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    mapper = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=["mapper"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["event", "song"], name="unique_song_per_event"
            )
        ]

    def save(self, *args, **kwargs):
        if not EventAttendee.objects.filter(
            event=self.event, attendee=self.mapper
        ).exists():
            raise ValidationError("The mapper is not an attendee of this event.")
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.song.song_title} ({self.song.artist}) played at {self.event.event_name} event"


class EventAttendee(models.Model):
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    attendee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    class Meta:
        unique_together = (
            "event",
            "attendee",
        )

    def __str__(self) -> str:
        return f"{self.attendee} is attending {self.event}"
