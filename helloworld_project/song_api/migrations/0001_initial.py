# Generated by Django 4.2.5 on 2024-02-15 22:57

import django.contrib.postgres.indexes
import django.contrib.postgres.search
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="SongCatalog",
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
                ("song_catalog_name", models.CharField(max_length=250, unique=True)),
                ("create_date", models.DateField(auto_now_add=True)),
                ("update_date", models.DateField(auto_now=True)),
                (
                    "song_catalog_owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Song",
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
                ("song_title", models.CharField(max_length=250)),
                ("artist", models.CharField(max_length=250)),
                ("album", models.CharField(blank=True, max_length=250, null=True)),
                ("genre", models.CharField(blank=True, max_length=250, null=True)),
                ("year", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "song_length",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                ("charter", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "intensity_bass",
                    models.IntegerField(
                        choices=[
                            (-1, "Not mapped for this instrument"),
                            (0, "Intensity level 0"),
                            (1, "Intensity level 1"),
                            (2, "Intensity level 2"),
                            (3, "Intensity level 3"),
                            (4, "Intensity level 4"),
                            (5, "Intensity level 5"),
                            (6, "Intensity level 6"),
                        ],
                        default=-1,
                    ),
                ),
                (
                    "intensity_bass_real",
                    models.IntegerField(
                        choices=[
                            (-1, "Not mapped for this instrument"),
                            (0, "Intensity level 0"),
                            (1, "Intensity level 1"),
                            (2, "Intensity level 2"),
                            (3, "Intensity level 3"),
                            (4, "Intensity level 4"),
                            (5, "Intensity level 5"),
                            (6, "Intensity level 6"),
                        ],
                        default=-1,
                    ),
                ),
                (
                    "intensity_bassghl",
                    models.IntegerField(
                        choices=[
                            (-1, "Not mapped for this instrument"),
                            (0, "Intensity level 0"),
                            (1, "Intensity level 1"),
                            (2, "Intensity level 2"),
                            (3, "Intensity level 3"),
                            (4, "Intensity level 4"),
                            (5, "Intensity level 5"),
                            (6, "Intensity level 6"),
                        ],
                        default=-1,
                    ),
                ),
                (
                    "intensity_drums",
                    models.IntegerField(
                        choices=[
                            (-1, "Not mapped for this instrument"),
                            (0, "Intensity level 0"),
                            (1, "Intensity level 1"),
                            (2, "Intensity level 2"),
                            (3, "Intensity level 3"),
                            (4, "Intensity level 4"),
                            (5, "Intensity level 5"),
                            (6, "Intensity level 6"),
                        ],
                        default=-1,
                    ),
                ),
                (
                    "intensity_drums_real",
                    models.IntegerField(
                        choices=[
                            (-1, "Not mapped for this instrument"),
                            (0, "Intensity level 0"),
                            (1, "Intensity level 1"),
                            (2, "Intensity level 2"),
                            (3, "Intensity level 3"),
                            (4, "Intensity level 4"),
                            (5, "Intensity level 5"),
                            (6, "Intensity level 6"),
                        ],
                        default=-1,
                    ),
                ),
                (
                    "intensity_drums_phase_shift",
                    models.IntegerField(
                        choices=[
                            (-1, "Not mapped for this instrument"),
                            (0, "Intensity level 0"),
                            (1, "Intensity level 1"),
                            (2, "Intensity level 2"),
                            (3, "Intensity level 3"),
                            (4, "Intensity level 4"),
                            (5, "Intensity level 5"),
                            (6, "Intensity level 6"),
                        ],
                        default=-1,
                    ),
                ),
                (
                    "intensity_guitar",
                    models.IntegerField(
                        choices=[
                            (-1, "Not mapped for this instrument"),
                            (0, "Intensity level 0"),
                            (1, "Intensity level 1"),
                            (2, "Intensity level 2"),
                            (3, "Intensity level 3"),
                            (4, "Intensity level 4"),
                            (5, "Intensity level 5"),
                            (6, "Intensity level 6"),
                        ],
                        default=-1,
                    ),
                ),
                (
                    "intensity_guitar_coop",
                    models.IntegerField(
                        choices=[
                            (-1, "Not mapped for this instrument"),
                            (0, "Intensity level 0"),
                            (1, "Intensity level 1"),
                            (2, "Intensity level 2"),
                            (3, "Intensity level 3"),
                            (4, "Intensity level 4"),
                            (5, "Intensity level 5"),
                            (6, "Intensity level 6"),
                        ],
                        default=-1,
                    ),
                ),
                (
                    "intensity_guitar_coop_ghl",
                    models.IntegerField(
                        choices=[
                            (-1, "Not mapped for this instrument"),
                            (0, "Intensity level 0"),
                            (1, "Intensity level 1"),
                            (2, "Intensity level 2"),
                            (3, "Intensity level 3"),
                            (4, "Intensity level 4"),
                            (5, "Intensity level 5"),
                            (6, "Intensity level 6"),
                        ],
                        default=-1,
                    ),
                ),
                (
                    "intensity_guitar_real",
                    models.IntegerField(
                        choices=[
                            (-1, "Not mapped for this instrument"),
                            (0, "Intensity level 0"),
                            (1, "Intensity level 1"),
                            (2, "Intensity level 2"),
                            (3, "Intensity level 3"),
                            (4, "Intensity level 4"),
                            (5, "Intensity level 5"),
                            (6, "Intensity level 6"),
                        ],
                        default=-1,
                    ),
                ),
                (
                    "intensity_guitarghl",
                    models.IntegerField(
                        choices=[
                            (-1, "Not mapped for this instrument"),
                            (0, "Intensity level 0"),
                            (1, "Intensity level 1"),
                            (2, "Intensity level 2"),
                            (3, "Intensity level 3"),
                            (4, "Intensity level 4"),
                            (5, "Intensity level 5"),
                            (6, "Intensity level 6"),
                        ],
                        default=-1,
                    ),
                ),
                (
                    "intensity_keys",
                    models.IntegerField(
                        choices=[
                            (-1, "Not mapped for this instrument"),
                            (0, "Intensity level 0"),
                            (1, "Intensity level 1"),
                            (2, "Intensity level 2"),
                            (3, "Intensity level 3"),
                            (4, "Intensity level 4"),
                            (5, "Intensity level 5"),
                            (6, "Intensity level 6"),
                        ],
                        default=-1,
                    ),
                ),
                (
                    "intensity_keys_real",
                    models.IntegerField(
                        choices=[
                            (-1, "Not mapped for this instrument"),
                            (0, "Intensity level 0"),
                            (1, "Intensity level 1"),
                            (2, "Intensity level 2"),
                            (3, "Intensity level 3"),
                            (4, "Intensity level 4"),
                            (5, "Intensity level 5"),
                            (6, "Intensity level 6"),
                        ],
                        default=-1,
                    ),
                ),
                (
                    "intensity_keys_phase_shift",
                    models.IntegerField(
                        choices=[
                            (-1, "Not mapped for this instrument"),
                            (0, "Intensity level 0"),
                            (1, "Intensity level 1"),
                            (2, "Intensity level 2"),
                            (3, "Intensity level 3"),
                            (4, "Intensity level 4"),
                            (5, "Intensity level 5"),
                            (6, "Intensity level 6"),
                        ],
                        default=-1,
                    ),
                ),
                (
                    "intensity_rhythm",
                    models.IntegerField(
                        choices=[
                            (-1, "Not mapped for this instrument"),
                            (0, "Intensity level 0"),
                            (1, "Intensity level 1"),
                            (2, "Intensity level 2"),
                            (3, "Intensity level 3"),
                            (4, "Intensity level 4"),
                            (5, "Intensity level 5"),
                            (6, "Intensity level 6"),
                        ],
                        default=-1,
                    ),
                ),
                (
                    "intensity_rhythm_ghl",
                    models.IntegerField(
                        choices=[
                            (-1, "Not mapped for this instrument"),
                            (0, "Intensity level 0"),
                            (1, "Intensity level 1"),
                            (2, "Intensity level 2"),
                            (3, "Intensity level 3"),
                            (4, "Intensity level 4"),
                            (5, "Intensity level 5"),
                            (6, "Intensity level 6"),
                        ],
                        default=-1,
                    ),
                ),
                ("create_date", models.DateTimeField(auto_now_add=True)),
                ("update_date", models.DateTimeField(auto_now=True)),
                (
                    "search_vector",
                    django.contrib.postgres.search.SearchVectorField(
                        blank=True, null=True
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
            options={
                "indexes": [
                    django.contrib.postgres.indexes.GinIndex(
                        fields=["search_vector"], name="song_api_so_search__cbc7fe_gin"
                    )
                ],
            },
        ),
    ]
