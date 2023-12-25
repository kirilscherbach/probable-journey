from django.contrib import admin

from .models import Song, SongCatalog

# Register your models here.
admin.site.register(Song)
admin.site.register(SongCatalog)
