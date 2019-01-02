from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Rule, Input, Output

"""In order to get around not have select.epoll in a windows environment we are implementing
Fake.RPi.GPIO which emulates the existence of the GPIO"""
try:
    import OPi.GPIO as GPIO
    fake = False
except ImportError:
    import FakeRPi.GPIO as GPIO
    fake = True
    print('The linux_interaction() function was not executed')

# Create your views here.

# Visual/GUI views


def index(request):
    """The home page for OR_web_GUI"""
    inputs = Input.objects.exclude(rule__text=None)
    outputs = Output.objects.exclude(rule__text=None)
    context = {'inputs': inputs, 'outputs': outputs, 'fake': fake}
    return render(request, 'OR_web_GUI/index.html', context)


def rules(request):
    """Shows the rules"""
    rules = Rule.objects.order_by('date_added')
    context = {'rules': rules, 'fake': fake}
    return render(request, 'OR_web_GUI/rules.html', context)


def inputs(request):
    """shows the inputs"""
    inputs = Input.objects.order_by('date_added')
    context = {'inputs': inputs, 'fake': fake}
    return render(request, 'OR_web_GUI/inputs.html', context)


def outputs(request):
    """shows those outputs"""
    outputs = Output.objects.order_by('date_added')
    context = {'outputs': outputs, 'fake': fake}
    return render(request, 'OR_web_GUI/outputs.html', context)


#  action views: basically there is no real reason hitting a url NEEDS to return a web page, that just what we do when
#  we let people use it, but we can have the 'view' do other things, like activate gpio pins


def relay_control(request, output_id):
    # Right now this code 'should' work, however what it really does is check for failing sytanx as all fake GPIO
    # reports as LOW kind of no matter what we do...only testing on a Pi will work.  Otherwise it simply flips the
    # current state and then calls the status request view
    """will grab the output sent to it and change the state of said output"""
    output = Output.objects.get(id=output_id)
    """sets up the PIN"""
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(output.channel, GPIO.OUT)
    """toggles the current state"""
    GPIO.output(output.channel, not GPIO.input(output.channel))
    GPIO.output(output.channel, GPIO.HIGH)
    """should return back to previous page"""
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/relaystatus/'+str(output_id)))


def relay_state(request, output_id):
    """will grab the output sent to it and return the state of said output"""
    output = Output.objects.get(id=output_id)
    state = GPIO.input(output.channel)
    if state:
        return render(request, 'OR_web_GUI/outputStateGreen.html')
    elif not state:
        return render(request, 'OR_web_GUI/outputStateRed.html')
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
