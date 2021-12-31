from django import forms

class AvatarForm(forms.Form):
    # name = forms.CharField()
    avatar_field = forms.ImageField()
