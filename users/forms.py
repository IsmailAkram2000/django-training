from django.contrib.auth.forms import UserChangeForm
from django import forms
from .models import User

class CustomUserChangeFrom(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = UserChangeForm.Meta.fields
        widgets = {
            'bio': forms.Textarea
        }