from django.contrib import admin
from .models import guest, Event_DB,userEvent
# Register your models here.
admin.site.register(guest)
admin.site.register(Event_DB)
admin.site.register(userEvent)