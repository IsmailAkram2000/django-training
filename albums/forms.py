from dataclasses import fields
from django import forms
from .models import Albums
from django.forms.widgets import DateInput

class albumForm(forms.ModelForm):
    class Meta:
        model = Albums
        fields = '__all__'

        help_texts = {
            'approved' : 'Approve the album if its name is not explicit'
        }  

        widgets = {
            'release_date' : DateInput(attrs={'type': 'date'}),
        }