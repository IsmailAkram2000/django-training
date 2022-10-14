import datetime
from email.policy import default
from django.utils import timezone
from django.db import models
from artists.models import Artist

class Albums(models.Model):
    artist = models.ForeignKey(Artist, on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length = 100, default = 'New Album')
    creation_date = models.DateTimeField(default = timezone.now)
    release_date =  models.DateTimeField(blank = False)
    cost = models.DecimalField(max_digits = 10, decimal_places = 2, blank = False)

    def __str__(self):
        return f"name: {self.name}, creation_date: {self.creation_date}, release_date: {self.release_date}, cost: {self.cost}"