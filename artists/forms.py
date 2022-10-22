from django import forms

class artistForm(forms.Form):
    Stage_name = forms.CharField(max_length = 100)
    Social_link = forms.URLField()