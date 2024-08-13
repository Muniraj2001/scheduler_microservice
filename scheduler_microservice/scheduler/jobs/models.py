from django.db import models
from django.utils import timezone

class Job(models.Model):
    name = models.CharField(max_length=255)
    schedule = models.CharField(max_length=255)
    last_run = models.DateTimeField(null=True, blank=True)
    next_run = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
