from django.db import models

class Artist(models.Model):
    Stage_name = models.CharField(unique = True, max_length = 100)
    Social_link = models.URLField(blank = True, default = "")

    def __str__(self):
        return f"Stage_name: {self.Stage_name},"

    def approved_albums(self):
        return self.albums_set.filter(approved = True).count()

    class Meta:
        ordering = ('Stage_name',)