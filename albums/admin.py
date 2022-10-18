from django.forms import ModelForm
from django.contrib import admin
from .models import Albums


class AlnumModel(admin.StackedInline):
    model = Albums

class AlbumForm(ModelForm):
    class Meta:
        help_texts = {'approved': "Approve the album if its name is not explicit",}

@admin.register(Albums)

class AlbumAdmin(admin.ModelAdmin):
    form = AlbumForm
    list_display=['artist','name','creation_date','release_date','cost','approved',]
    readonly_fields=['creation_date']