# Generated by Django 4.2.5 on 2023-11-29 15:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("song_api", "0008_song_create_date_song_update_date_and_more"),
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
            ],
        ),
        migrations.CreateModel(
            name="EventPlan",
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
                    "song",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="song_api.song",
                    ),
                ),
            ],
        ),
    ]
