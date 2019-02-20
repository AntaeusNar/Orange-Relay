# django imports
from django.shortcuts import render
from django.http import HttpResponseRedirect

# local imports
from OR_web_GUI.models import Output
from .hidden import relay_control, follow_the_rules


# import for GPIO in real vs. test env
try:
    import OPi.GPIO as GPIO
    fake = False
except ImportError:
    from OR_web_GUI.packages import extendGPIO as GPIO
    fake = True
    print('The linux_interaction() function was not executed')


def state_toggle(request, whichmodel, key_id):
    if whichmodel == 'Output':
        relay_control(key_id)
    elif whichmodel == 'Input':
        # todo: add state changes based on rules or inputs
        fish
    elif whichmodel == 'Rule':
        follow_the_rules(key_id)
        """should return back to previous page"""
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


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

