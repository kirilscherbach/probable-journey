# Generated by Django 4.2.5 on 2023-11-29 16:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("song_api", "0008_song_create_date_song_update_date_and_more"),
        ("event_api", "0003_rename_eventplan_eventtosongmapping"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="EventToSongMapping",
            new_name="SongAtEventMapping",
        ),
    ]
