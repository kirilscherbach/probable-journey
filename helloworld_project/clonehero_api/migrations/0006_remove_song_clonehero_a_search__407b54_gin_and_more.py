# Generated by Django 4.2.5 on 2023-11-12 17:04

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("clonehero_api", "0005_song_search_vector_and_more"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="song",
            name="clonehero_a_search__407b54_gin",
        ),
        migrations.RemoveField(
            model_name="song",
            name="search_vector",
        ),
        migrations.AddField(
            model_name="song",
            name="search_vector_upd",
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
        migrations.AddIndex(
            model_name="song",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["search_vector_upd"], name="clonehero_a_search__e10779_gin"
            ),
        ),
    ]
