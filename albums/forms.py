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

    def clean_cost(self):
        cost = self.cleaned_data.get('cost')

        if(cost <= 0):
            raise forms.ValidationError('The cost must be larger than 0.')
        return cost
            