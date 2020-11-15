from django.contrib import admin
from .models import Eventtype, Organizer, Eventlocation, Event

admin.site.register(Eventtype)
admin.site.register(Organizer)
admin.site.register(Eventlocation)
admin.site.register(Event)


