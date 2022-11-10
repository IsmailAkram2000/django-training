from rest_framework import serializers
from artists.serializers import ArtistSerializer
from .models import Albums

class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Albums
        fields = ['id', 'artist', 'name', 'release_date', 'cost']

