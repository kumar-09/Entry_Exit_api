from django.db import models

# Create your models here.
from django.db import models


class Guests(models.Model):
    name = models.CharField(max_length=100)
    userid = models.CharField(max_length=14, primary_key=True)
    email_id = models.CharField(max_length=120)
    pswd = models.CharField(max_length=30)
    phone_num = models.CharField(max_length=12)

    def _str_(self):
        return self.name

    def _str_(self):
        return self.email_id

    def _str_(self):
        return self.phone_num


class Event_DB(models.Model):
    event_name = models.CharField(max_length=150)
    event_id = models.IntegerField(max_length=30)
    event_time = models.CharField(max_length=50)
    event_location = models.CharField(max_length=100)

    def _str_(self):
        return self.event_name

    def _str_(self):
        return self.event_time


class userEvent(models.Model):
    userid = models.ForeignKey(Guests, on_delete=models.CASCADE, default=0)
    event_id = models.CharField(max_length=100, default=0)
    registered = models.BooleanField(default=False)
    attended = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.userid


class GeneratedPrime(models.Model):
    value = models.PositiveIntegerField()
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.value)
