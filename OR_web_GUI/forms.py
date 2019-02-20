from django import forms

from .models import Output, Rule, Input


class OutputForm(forms.ModelForm):
    class Meta:
        model = Output
        fields = ['text', 'channel']
        labels = {'text': 'Description of Output', 'channel': 'Channel Number'}


class RulesForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields = ['text', 'input', 'output', 'action', 'times', 'length']
        labels = {'input': 'Triggering Input', 'output': 'Triggered Output', 'text': 'Description of Rule',
                  'times': 'Length of action', 'length': 'Timer'}


class InputForm(forms.ModelForm):
    class Meta:
        model = Input
        fields = {'text'}

