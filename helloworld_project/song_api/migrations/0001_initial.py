# Generated by Django 4.2.5 on 2023-11-12 15:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
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
                ("album", models.CharField(max_length=250)),
                ("genre", models.CharField(max_length=250)),
                ("year", models.IntegerField()),
                ("song_length", models.CharField(max_length=250)),
                ("charter", models.CharField(max_length=250)),
                ("intensity_guitar", models.IntegerField()),
                ("intensity_rhythm", models.IntegerField()),
                ("intensity_bass", models.IntegerField()),
                ("intensity_guitar_coop", models.IntegerField()),
                ("intensity_drums", models.IntegerField()),
                ("intensity_drums_real", models.IntegerField()),
                ("intensity_guitarghl", models.IntegerField()),
                ("intensity_bassghl", models.IntegerField()),
                ("intensity_rhythm_ghl", models.IntegerField()),
                ("intensity_guitar_coop_ghl", models.IntegerField()),
                ("intensity_keys", models.IntegerField()),
            ],
        ),
    ]