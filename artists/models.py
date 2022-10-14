from email.policy import default
from django.db import models

class Artist(models.Model):
    Stage_name = models.CharField(unique = True, max_length = 100)
    Social_link = models.URLField(blank = True, default = "")

    def __str__(self):
        return f"Stage_name: {self.Stage_name}, Social_link: {self.Social_link}"
    
    class Meta:
        ordering = ('Stage_name',)