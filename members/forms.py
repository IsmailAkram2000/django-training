from django import forms

class loginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)