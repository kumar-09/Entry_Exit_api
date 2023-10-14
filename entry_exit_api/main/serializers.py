from rest_framework import serializers
from .models import guest, Event_DB, userEvent


class guestSerializer(serializers.ModelSerializer):
    class Meta:
        model = guest
        fields = ['name', 'userid', 'email_id', 'pswd', 'phone_num']


class Event_DBSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event_DB
        fields = ['event_name', 'event_id', 'event_time', 'event_location']


class userEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = userEvent
        fields = ['userid']
