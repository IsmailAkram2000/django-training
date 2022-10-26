from django import forms
from .models import Artist

class artistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'

    def clean_Stage_name(self):
        Stage_name = self.cleaned_data.get('Stage_name')
        query = Artist.objects.filter(Stage_name = Stage_name).count()

        if(query > 0):
            raise forms.ValidationError('Stage name must be unique.')
        return Stage_name