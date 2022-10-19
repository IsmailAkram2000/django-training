from django import forms
from django.contrib import admin
from .models import Albums

class AlbumsInline(admin.StackedInline):
    model = Albums

class AlbumForm(forms.ModelForm):
    class Meta:
        help_texts = {'approved': "Approve the album if its name is not explicit",}

class AlbumAdmin(admin.ModelAdmin):
    form = AlbumForm
    list_display=['artist','name','creation_date','release_date','cost','approved',]
    readonly_fields=['creation_date']

admin.site.register(Albums, AlbumAdmin)