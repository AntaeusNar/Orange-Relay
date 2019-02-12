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
        fields = ['input', 'output', 'text']
        labels = {'input': 'Triggering Input', 'output': 'Triggered Output', 'text': 'Description of Rule'}


class LinkingLogic(forms.FORM):
    # this form should allow the user to select an input and condition and then set an output state
    input = forms.ModelChoiceField(queryset=Input)
