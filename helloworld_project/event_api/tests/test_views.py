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


@pytest.mark.django_db
def test_event_attendee_list_unauthenticated():
    client = APIClient()
    url = reverse("event_attendees")
    response = client.get(url)
    assert (
        response.status_code == 401
    )  # Unauthenticated users should get a 403 response


@pytest.mark.django_db
def test_event_attendee_list_authenticated():
    client = APIClient()
    # Create a test user and log them in
    user = mixer.blend(User)
    client.force_authenticate(user=user)

    # Create an event with the user as the organizer
    event = mixer.blend(Event, event_organizer=user)

    # Create an EventAttendee instance for the event
    mixer.blend(EventAttendee, event=event)

    url = reverse("event_attendees")
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1  # The user should see one event attendee


@pytest.mark.django_db
def test_event_attendee_list_create():
    client = APIClient()
    # Create a test user and log them in
    user = mixer.blend(User)
    client.force_authenticate(user=user)

    # Create an event with the user as the organizer
    event = mixer.blend(Event, event_organizer=user)

    # Create another user to be the attendee
    attendee = mixer.blend(User)

    url = reverse("event_attendees")
    data = {"event": event.pk, "attendee": attendee.pk}
    response = client.post(url, data)
    assert response.status_code == 201  # The creation should be successful
    assert EventAttendee.objects.count() == 1


@pytest.mark.django_db
def test_event_attendee_list_create_not_organizer():
    client = APIClient()
    # Create a test user and log them in
    user = mixer.blend(User)
    client.force_authenticate(user=user)

    # Create an event with a different user as the organizer
    event = mixer.blend(Event, event_organizer=mixer.blend(User))

    # Create another user to be the attendee
    attendee = mixer.blend(User)

    url = reverse("event_attendees")
    data = {"event": event.pk, "attendee": attendee.pk}
    response = client.post(url, data)
    assert (
        response.status_code == 403
    )  # The user should not be allowed to create the event attendee
