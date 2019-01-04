#  This file should only load AFTER FakeRPi.GPIO is loaded, if that one is needed.  Here we are wanted to overide some
#  functionality of the FakeRPi.GPIO to give a little bit more of an emulation.  honestly this probely needs to be
#  forked and rewritten as a separate package for dev work, but here we are.....

# The basic idea is that when a pin is made HIGH or LOW it is writen into a file,
# and then when the input is checked it reads the file.......

from FakeRPi.GPIO import *
from . import extendJSON as JSON


def output(channel, state):
    """
    To set the output state of a GPIO pin:
    :param channel:
    :return:
    """

    # should try to open the json file containing the pin dict with error handling options
    try:
        JSON.getJSONfile('pins.json')
    except EnvironmentError:
        pins = {}

    pins[channel] = state

    JSON.writeJSONfile('pins.json', pins)

    return state
