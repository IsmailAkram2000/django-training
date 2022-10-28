from django import forms
from django.contrib import admin
from .models import Albums, Song

class AlbumsInline(admin.StackedInline):
    model = Albums

class SongInline(admin.StackedInline):
    model = Song
    min_num = 1

class AlbumForm(forms.ModelForm):
    class Meta:
        help_texts = {'approved': "Approve the album if its name is not explicit",}

class AlbumAdmin(admin.ModelAdmin):
    form = AlbumForm
    inlines = [SongInline]
    readonly_fields = ['created']
    list_display=['artist','name','release_date','cost','approved',]

class SongAdmin(admin.ModelAdmin):
    list_display = ['album', 'name', 'image', 'image_thumbnail', 'audio'] 

admin.site.register(Albums, AlbumAdmin)
admin.site.register(Song, SongAdmin)