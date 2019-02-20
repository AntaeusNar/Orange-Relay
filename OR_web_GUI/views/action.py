# django imports
from django.http import HttpResponseRedirect

# local imports
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
        # todo: add state changes based on inputs
        fish
    elif whichmodel == 'Rule':
        follow_the_rules(key_id)
        """should return back to previous page"""
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

