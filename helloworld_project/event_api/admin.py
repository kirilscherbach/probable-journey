from django.contrib import admin

from .models import Event, EventPlan

admin.site.register(Event)
admin.site.register(EventPlan)
