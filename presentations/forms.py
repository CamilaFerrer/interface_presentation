from django import forms
from .models import Presentation, Slide

class PresentationForm(forms.ModelForm):
    class Meta:
        model = Presentation
        fields = ['title', 'description']
        exclude = ["author"]

class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = ['content']

