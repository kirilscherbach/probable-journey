import datetime
from datetime import date

import pytest
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from event_api.models import Event, EventAttendee, SongAtEventMapping
from freezegun import freeze_time
from mixer.backend.django import mixer
from song_api.models import Song, SongCatalog


@pytest.mark.django_db
def test_event_creation():
    user = mixer.blend(User)
    song_catalog = mixer.blend(SongCatalog)
    event = Event.objects.create(
        event_name="Test Event",
        event_date=date.today(),
        song_catalog=song_catalog,
        event_organizer=user,
    )
    assert isinstance(event, Event)
    assert event.event_name == "Test Event"
    assert event.event_date == date.today()
    assert event.song_catalog == song_catalog
    assert event.event_organizer == user


@pytest.mark.django_db
def test_event_str():
    user = mixer.blend(User)
    song_catalog = mixer.blend(SongCatalog)
    event = Event.objects.create(
        event_name="Test Event",
        event_date=date.today(),
        song_catalog=song_catalog,
        event_organizer=user,
    )
    assert str(event) == f"Test Event at {date.today()}"


@pytest.mark.django_db
def test_song_at_event_mapping_creation():
    user = mixer.blend(User)
    event = mixer.blend(Event, event_organizer=user)
    song = mixer.blend(Song)
    EventAttendee.objects.create(event=event, attendee=user)
    mapping = SongAtEventMapping.objects.create(
        event=event,
        song=song,
        mapper=user,
    )
    assert isinstance(mapping, SongAtEventMapping)
    assert mapping.event == event
    assert mapping.song == song
    assert mapping.mapper == user


@pytest.mark.django_db
def test_song_at_event_mapping_str():
    user = mixer.blend(User)
    event = mixer.blend(Event, event_organizer=user)
    song = mixer.blend(Song, song_title="Test Song", artist="Test Artist")
    EventAttendee.objects.create(event=event, attendee=user)
    mapping = SongAtEventMapping.objects.create(
        event=event,
        song=song,
        mapper=user,
    )
    assert str(mapping) == "Test Song (Test Artist) played at {} event".format(
        event.event_name
    )


@pytest.mark.django_db
def test_song_at_event_mapping_save_validation():
    user = mixer.blend(User)
    event = mixer.blend(Event, event_organizer=user)
    song = mixer.blend(Song)
    mapping = SongAtEventMapping(
        event=event,
        song=song,
        mapper=user,
    )
    with pytest.raises(ValidationError):
        mapping.save()  # This should raise a ValidationError because the mapper is not an attendee of the event


@pytest.mark.django_db
def test_event_attendee_creation():
    user = mixer.blend(User)
    event = mixer.blend(Event, event_organizer=user)
    attendee = EventAttendee.objects.create(
        event=event,
        attendee=user,
    )
    assert isinstance(attendee, EventAttendee)
    assert attendee.event == event
    assert attendee.attendee == user


@pytest.mark.django_db
def test_event_attendee_unique_constraint():
    user = mixer.blend(User)
    event = mixer.blend(Event, event_organizer=user)
    EventAttendee.objects.create(event=event, attendee=user)
    with pytest.raises(IntegrityError):
        EventAttendee.objects.create(
            event=event, attendee=user
        )  # This should raise a IntegrityError because an EventAttendee with the same event and attendee already exists


@pytest.mark.django_db
@freeze_time("2022-01-01")
def test_model_creation():
    user = mixer.blend(User)
    event = mixer.blend(Event, event_organizer=user)
    attendee = EventAttendee.objects.create(
        event=event,
        attendee=user,
    )
    assert attendee.create_date == datetime.date(2022, 1, 1)


@pytest.mark.django_db
@freeze_time("2022-01-01")
def test_event_attendee_str():
    user = mixer.blend(User, username="testuser")
    song_catalog = mixer.blend(SongCatalog)
    event = Event.objects.create(
        event_name="Test Event Str",
        event_date=date.today(),
        song_catalog=song_catalog,
        event_organizer=user,
    )
    attendee = EventAttendee.objects.create(
        event=event,
        attendee=user,
    )
    assert attendee.create_date == datetime.date(2022, 1, 1)
    assert str(attendee) == "testuser is attending Test Event Str on 2022-01-01"
