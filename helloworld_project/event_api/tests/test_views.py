import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from event_api.models import Event, EventAttendee, SongAtEventMapping
from mixer.backend.django import mixer
from rest_framework.test import APIClient
from song_api.models import Song


@pytest.mark.django_db
def test_event_list():
    client = APIClient()
    url = reverse("events")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_event_detail():
    client = APIClient()
    # Create a test user and log them in
    user = mixer.blend(User)
    client.force_authenticate(user=user)

    event = mixer.blend(Event)
    url = reverse("events_detail", kwargs={"pk": event.pk})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_song_at_event_mapping_list():
    client = APIClient()
    url = reverse("mappings")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_song_at_event_mapping_detail():
    client = APIClient()
    # Create a test user and log them in
    user = mixer.blend(User)
    client.force_authenticate(user=user)

    # Create an event and add the user as an attendee
    event = mixer.blend(Event)
    EventAttendee.objects.create(
        event=event, attendee=user
    )  # Create an EventAttendee instance

    # Create a SongAtEventMapping instance with the user as the mapper
    song_at_event_mapping = SongAtEventMapping.objects.create(
        event=event, mapper=user, song=mixer.blend(Song)
    )

    url = reverse("mappings_detail", kwargs={"pk": song_at_event_mapping.pk})
    response = client.get(url)
    assert response.status_code == 200
