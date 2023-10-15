from django.contrib import admin
from .models import Guests, Event_DB, userEvent, GeneratedPrime
# Register your models here.
admin.site.register(Guests)
admin.site.register(Event_DB)
admin.site.register(userEvent)
admin.site.register(GeneratedPrime)
