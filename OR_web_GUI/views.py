from django.shortcuts import render
from .models import Rule, Input

# Create your views here.


def index(request):
    """The home page for OR_web_GUI"""
    return render(request, 'OR_web_GUI/index.html')


def rules(request):
    """Shows the rules"""
    rules = Rule.objects.order_by('date_added')
    context = {'rules': rules}
    return render(request, 'OR_web_GUI/rules.html', context)


def inputs(request):
    """shows the inputs"""
    inputs = Input.objects.order_by('date_added')
    context = {'inputs': inputs}
    return render(request, 'OR_web_GUI/inputs.html', context)
