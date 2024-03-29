# Generated by Django 4.2.5 on 2024-02-15 21:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("song_api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("event_name", models.CharField(max_length=250, unique=True)),
                ("event_date", models.DateField()),
                ("create_date", models.DateField(auto_now_add=True)),
                ("update_date", models.DateField(auto_now=True)),
                (
                    "event_organizer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "song_catalog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="song_api.songcatalog",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EventAttendee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("create_date", models.DateField(auto_now_add=True)),
                ("update_date", models.DateField(auto_now=True)),
                (
                    "attendee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attended_events",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="event_api.event",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SongAtEventMapping",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="event_api.event",
                    ),
                ),
                (
                    "mapper",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "song",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="song_api.song"
                    ),
                ),
            ],
            options={
                "indexes": [
                    models.Index(
                        fields=["mapper"], name="event_api_s_mapper__edcc49_idx"
                    )
                ],
            },
        ),
        migrations.AddConstraint(
            model_name="songateventmapping",
            constraint=models.UniqueConstraint(
                fields=("event", "song"), name="unique_song_per_event"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="eventattendee",
            unique_together={("event", "attendee")},
        ),
    ]
