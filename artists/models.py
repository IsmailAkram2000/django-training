from django.db import models
from users.models import User

class Artist(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null=True)
    Stage_name = models.CharField(unique = True, max_length = 100)
    Social_link = models.URLField(blank = True, default = "")

    def __str__(self):
        return f"Stage_name: {self.Stage_name}, Social_link: {self.Social_link}"

    def approved_albums(self):
        return self.albums_set.filter(approved = True).count()

    class Meta:
        ordering = ('Stage_name',)