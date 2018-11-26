from django.shortcuts import render
from django.http import HttpResponseRedirect
import OPi.GPIO as GPIO
from .models import Rule, Input, Output

# Create your views here.

# Visual/GUI views

def index(request):
    """The home page for OR_web_GUI"""
    inputs = Input.objects.exclude(rule__text=None)
    outputs = Output.objects.exclude(rule__text=None)
    context = {'inputs': inputs, 'outputs' : outputs}
    return render(request, 'OR_web_GUI/index.html', context)


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


def outputs(request):
    """shows those outputs"""
    outputs = Output.objects.order_by('date_added')
    context = {'outputs': outputs}
    return render(request, 'OR_web_GUI/outputs.html', context)


#  action views: basically there is no real reason hitting a url NEEDS to return a webpage, that just what we do when
#  we let people use it, but we can have the 'view' do other things, like activate gpio pins


def relay_control(request, output_id):
    """will grab the output sent to it and change the state of said output"""
    output = Output.objects.get(id=output_id)
    """sets up the PIN"""
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(output.channel, GPIO.OUT)
    """toggles the current"""
    GPIO.output(output.channel, not GPIO.input(output.channel))
    """should return back to previous page"""
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
