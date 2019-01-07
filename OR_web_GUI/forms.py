from django import forms

from .models import Output


class OutputForm(forms.ModelForm):
    class Meta:
        model = Output
        fields = ['text', 'channel']
        labels = {'text': 'Description of Output', 'channel': 'Channel Number'}
