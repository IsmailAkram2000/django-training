from django.db import models
from artists.models import Artist
from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from albums.tasks import send_mail_task
from django.dispatch import receiver 
from django.db.models.signals import post_save 

class Albums(TimeStampedModel):
    artist = models.ForeignKey(Artist, on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length = 100, default = 'New Album')
    release_date =  models.DateTimeField(blank = False)
    cost = models.DecimalField(max_digits = 10, decimal_places = 2, blank = False)
    approved = models.BooleanField(default = False)

    def __str__(self):
        return f"name: {self.name}, release_date: {self.release_date}, cost: {self.cost}"

@receiver(post_save, sender=Albums)
def album_post_save(sender, instance,  *args, **kwargs):
    send_mail_task.delay(instance.name, instance.artist.id) 

class Song(models.Model):
    album = models.ForeignKey(Albums, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=True)
    image = models.ImageField(upload_to='files')
    # I think image_thumbnail field is unnecessary it just going to take more space, If i need to display all songs in album I could just use the image and resize it.
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(100, 50)], format='JPEG', options={'quality': 60})
    audio = models.FileField(upload_to='files', validators=[FileExtensionValidator(['mp3', 'wav'])])

    def save(self):
        if self.name == '':
            self.name = self.album.name
        return super().save()

    def delete(self, *args, **kwargs):
        num_of_songs = (self.album.song_set.all().count() > 1)
        if num_of_songs:
            super(Song, self).delete(*args, **kwargs)
        else:
            raise ValidationError('Can\'t delete this song, An album must have at least one song.')