from django import forms
from .models import Property, photo

class PropertyFieldworkForm(forms.ModelForm):
    class Meta:
        model = photo
        exclude = []
        fields = ['prop', 'image', 'description']
