"""Interactive url callable views with no forward facing display"""

# django imports
from django.http import HttpResponseRedirect
from django.template.defaulttags import register
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

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
    # Usage: in template -> {{ mydict|get_item:item.NAME }}


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

