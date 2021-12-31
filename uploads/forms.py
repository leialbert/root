from django import forms
from django.forms import fields

from uploads.models import Author

class AvatarForm(forms.Form):
    class Meta:
        model = Author
        field = '__all__'
