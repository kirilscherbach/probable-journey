from django.contrib import admin

from .models import Event, EventAttendee, SongAtEventMapping

admin.site.register(Event)
admin.site.register(SongAtEventMapping)
admin.site.register(EventAttendee)
