from django.contrib import admin

from .models import Event, SongAtEventMapping

admin.site.register(Event)
admin.site.register(SongAtEventMapping)
