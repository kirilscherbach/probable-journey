# Generated by Django 4.2.5 on 2023-12-25 20:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("song_api", "0011_song_song_catalog"),
        ("event_api", "0005_songateventmapping_mapper_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="song_catalog",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                to="song_api.songcatalog",
            ),
            preserve_default=False,
        ),
    ]
