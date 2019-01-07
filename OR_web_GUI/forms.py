from django import forms

from .models import output


class OutputForm(forms.ModelForm):
    class Meta:
        model = output
        fields = ['text', 'int']
        labels = {'text': '', 'int': ''}
