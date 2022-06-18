from operator import mod
from statistics import mode
from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255)
    time_from = models.DateTimeField()
    time_to = models.DateTimeField()
    remind_before = models.TimeField()
    group_of_recipients = models.CharField(max_length=255)
    place = models.CharField(max_length=255)

    content = models.TextField(blank=True)

    notes = models.TextField()

    def __str__(self) -> str:
        return self.name
