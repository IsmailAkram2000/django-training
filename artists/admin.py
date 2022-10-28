from django.contrib import admin
from .models import Artist
from albums.admin import AlbumsInline

class ArtistAdmin(admin.ModelAdmin):
    list_display = ["Stage_name", "Social_link", "approved_albums"]

admin.site.register(Artist, ArtistAdmin)
