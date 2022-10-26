from django.db import models
from artists.models import Artist
from model_utils.models import TimeStampedModel

class Albums(TimeStampedModel):
    artist = models.ForeignKey(Artist, on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length = 100, default = 'New Album')
    release_date =  models.DateTimeField(blank = False)
    cost = models.DecimalField(max_digits = 10, decimal_places = 2, blank = False)
    approved = models.BooleanField(default = False)

    def __str__(self):
        return f"name: {self.name}, release_date: {self.release_date}, cost: {self.cost}"