from dataclasses import field
from django import forms
from .models import Artist

class artistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'

    def clean_Stage_name(self):
        Stage_name = self.cleaned_data.get('Stage_name')
        print(Stage_name)

        if(Stage_name == 'A'):
            raise forms.ValidationError('Change stage name .')
        return Stage_name